# cURL examples

## Chat completion

```bash
curl https://api.cheapaimodel.com/v1/chat/completions \
  -H "Authorization: Bearer $CHEAPAIMODEL_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-4o-mini",
    "messages": [{"role": "user", "content": "Hello!"}]
  }'
```

## Streaming

```bash
curl -N https://api.cheapaimodel.com/v1/chat/completions \
  -H "Authorization: Bearer $CHEAPAIMODEL_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-4o-mini",
    "stream": true,
    "messages": [{"role": "user", "content": "Count to 5"}]
  }'
```

## List models

```bash
curl https://api.cheapaimodel.com/v1/models \
  -H "Authorization: Bearer $CHEAPAIMODEL_API_KEY"
```
