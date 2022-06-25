docker-build:
	docker buildx build --tag docx_to_web --load .

docker-arm64-build:
	docker buildx build --tag docx_to_web --load --platform linux/arm64 .

docker-run:
	docker run -p 8080:8080 docx_to_web