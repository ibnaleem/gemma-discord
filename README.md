# Discord Bot Gemma
The implementation of [Gemma, a new open model developed by Google and its DeepMind team,](https://huggingface.co/google/gemma-7b) as a Discord bot.

The models are trained using a diverse dataset of web documents, exposing them to a broad spectrum of linguistic styles, topics, and vocabularies. This encompasses code to comprehend syntax and patterns of programming languages, as well as mathematical text to understand logical reasoning.

In order to safeguard the model, the team implemented several data cleaning and filtering methods, including stringent filtering for CSAM (child sexual abuse material), sensitive data filtering, and content quality-based filtering in accordance with Google’s policies.

## Invite Gemma
Gemma does not require any permissions, it is a **chat-only** Discord bot:
```
https://discord.com/oauth2/authorize?client_id=1211309998454476851&permissions=0&scope=bot
```

## Privacy
- Gemma (Discord bot) only stores your chats in random access memory (RAM) ([L40-43](https://github.com/ibnaleem/gemma-discord/blob/main/main.py#L40C15-L43C74)).

## Acknowledgements
- [Google DeepMind](https://deepmind.google)
- [Gemma Open Model](https://huggingface.co/google/gemma-7b)
- [ollama/ollama-python](https://github.com/ollama/ollama-python)

## Support Server
```
Coming Soon
```
