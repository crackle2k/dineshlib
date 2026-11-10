import { Client, Events, GatewayIntentBits, MessageFlags } from 'discord.js';
import { requireEnv } from './config.js';
import { startMeetingReminders } from './meeting-reminders.js';

const token = requireEnv('DISCORD_TOKEN');
const client = new Client({ intents: [GatewayIntentBits.Guilds] });

client.once(Events.ClientReady, readyClient => {
  console.log(`Logged in as ${readyClient.user.tag}`);
  startMeetingReminders(readyClient);
});

client.on(Events.InteractionCreate, async interaction => {
  if (!interaction.isChatInputCommand() || interaction.commandName !== 'ping') return;

  try {
    await interaction.reply('Pong!');
  } catch (error) {
    console.error('Failed to respond to /ping:', error);
    try {
      if (!interaction.replied && !interaction.deferred) {
        await interaction.reply({ content: 'Something went wrong. Try again.', flags: MessageFlags.Ephemeral });
      }
    } catch (replyError) {
      console.error('Failed to send the error response:', replyError);
    }
  }
});

client.on(Events.Error, error => console.error('Discord client error:', error));

for (const signal of ['SIGINT', 'SIGTERM']) {
  process.once(signal, () => {
    client.destroy();
    process.exit(0);
  });
}

try {
  await client.login(token);
} catch (error) {
  console.error('Could not log in to Discord:', error);
  client.destroy();
  process.exitCode = 1;
}
