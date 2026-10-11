import { REST, Routes, SlashCommandBuilder } from 'discord.js';
import { requireEnv } from './config.js';

const token = requireEnv('DISCORD_TOKEN');
const clientId = requireEnv('DISCORD_CLIENT_ID');
const guildId = requireEnv('DISCORD_GUILD_ID');
const rest = new REST({ version: '10' }).setToken(token);
const ping = new SlashCommandBuilder().setName('ping').setDescription('Replies with Pong!');

try {
  await rest.post(Routes.applicationGuildCommands(clientId, guildId), { body: ping.toJSON() });
  console.log(`Registered /ping in server ${guildId}.`);
} catch (error) {
  console.error('Could not register /ping:', error);
  process.exitCode = 1;
}
