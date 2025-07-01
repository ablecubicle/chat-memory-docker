# chat-memory-docker

A Python FastAPI app (Dockerized) that lets you:
- Store your OpenAI chat history and preferences persistently.
- Search, review, and reuse your own chat history as context.
- Proxy queries to the OpenAI API with your own API key.

## Usage

1. Clone/download this repo.
2. **Set your OpenAI API key** as an environment variable:
    ```
    export OPENAI_API_KEY="your-key-here"
    ```
   Or, set it in your docker-compose environment.

3. Build and run with Docker Compose:
    ```
    docker compose up --build
    ```

4. App runs at [http://localhost:8001](http://localhost:8001) by default.

## Privacy

- **Your API key is NEVER stored in code or database.**
- **Your chat history and preferences are stored in `app/data/chat_memory.db`, which is gitignored by default for your privacy.**

## Protect your data and API keys!

- The database file (`app/data/`, `app/chat_memory.db`) and any `.env` files are NOT included in this repo for privacy/security reasons.
- To use this app, set your `OPENAI_API_KEY` as an environment variable before running or add it to a `.env` file (not committed).


## Contributions

PRs welcome!

---

*If you use this, you’re responsible for your own API usage and OpenAI costs. See LICENSE for details.*
