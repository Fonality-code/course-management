from app import app
from initialize import main
import asyncio


if __name__ == "__main__":
    asyncio.run(main())
    app.run(debug=True, host="0.0.0.0")
