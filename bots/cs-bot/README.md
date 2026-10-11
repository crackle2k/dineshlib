# cs-bot

A small discord.js bot that replies to `/ping` with `Pong!`.

## Setup

Requires Node.js **24.17.0 or newer**.

1. Create an application in the [Discord Developer Portal](https://discord.com/developers/applications).
2. Open its **Bot** page and generate a bot token. Keep the token private.
3. Copy the **Application ID** from **General Information**.
4. In Discord, enable **Developer Mode** under **User Settings → Advanced**, then right-click your test server and select **Copy Server ID**.
5. In the application's **OAuth2 → URL Generator**, select the `bot` and `applications.commands` scopes. Open the generated URL to invite the bot to your test server. No privileged intents or Administrator permission are needed for this command.
6. From this repository, run:

   ```sh
   cd bots/cs-bot
   npm install
   cp .env.example .env
   ```

7. Fill in `.env`:

   ```dotenv
   DISCORD_TOKEN=your_bot_token
   DISCORD_CLIENT_ID=your_application_id
   DISCORD_GUILD_ID=your_test_server_id
   ```

8. Register the command and start the bot:

   ```sh
   npm run deploy-commands
   npm start
   ```

Use `/ping` in your test server. Keep the bot process running to answer commands.

The command is registered only in the configured test server. Run `deploy-commands` again after changing its definition; restarting the bot alone does not update registered commands. Registering `/ping` updates that command without deleting other commands.

## Development

- `src/index.js` handles Discord events and command replies.
- `src/deploy-commands.js` registers the slash command.
- `npm run check` checks JavaScript syntax.

`.env` and `node_modules` are ignored by Git. Environment variables supplied by your host also work without an `.env` file.
