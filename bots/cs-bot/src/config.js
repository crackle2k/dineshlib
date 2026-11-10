export function requireEnv(name) {
  const value = process.env[name]?.trim();
  if (!value) {
    throw new Error(`Missing ${name}. Please set the ${name} environment variable.`);
  }
  return value;
}
