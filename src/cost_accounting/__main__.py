import uvicorn

from .settings import settings

uvicorn.run(
	'cost_accounting.app:app',
	host=settings.server_host,
	port=settings.server_port,
	reload=True,
)
