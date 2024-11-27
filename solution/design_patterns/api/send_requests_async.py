import httpx
import asyncio


BASE_URL = "http://localhost:8000/count_words"

async def main():
    # run multiple requests concurrently
    start_time = asyncio.get_event_loop().time()
    async with httpx.AsyncClient() as client:
        tasks = [
                client.post(
                    BASE_URL,
                    json={"text": " ".join(["hello"] * i)},
                    timeout=None
                    )
                for i in range(1, 11)]
        responses = await asyncio.gather(*tasks)
        for response in responses:
            print(response.text)

    end_time = asyncio.get_event_loop().time()
    print(f"Time taken: {end_time - start_time}")


asyncio.run(main())