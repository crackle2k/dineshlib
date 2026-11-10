const channelId = '1409274112232263701';
const roleId = '1409258614224326706';

const reminders = {
  '11:00': 'CS Club executive meeting today at **8:00 p.m. Eastern time**.',
  '19:50': 'The CS Club executive meeting starts in **10 minutes**, at **8:00 p.m. Eastern time**.',
};

const torontoTime = new Intl.DateTimeFormat('en-CA', {
  timeZone: 'America/Toronto',
  weekday: 'short',
  year: 'numeric',
  month: '2-digit',
  day: '2-digit',
  hour: '2-digit',
  minute: '2-digit',
  hourCycle: 'h23',
});

export function startMeetingReminders(client) {
  let lastSent;
  let sending = false;

  async function checkReminder() {
    const { weekday, year, month, day, hour, minute } = Object.fromEntries(
      torontoTime.formatToParts(new Date()).map(({ type, value }) => [type, value]),
    );
    const message = reminders[`${hour}:${minute}`];
    if (weekday !== 'Sun' || !message || sending) return;

    const nonce = `cs-exec-${year}${month}${day}${hour}${minute}`;
    if (nonce === lastSent) return;

    sending = true;
    try {
      const channel = await client.channels.fetch(channelId);
      if (!channel?.isSendable()) throw new Error(`Cannot send to channel ${channelId}`);

      await channel.send({
        content: `<@&${roleId}> ${message}`,
        allowedMentions: { parse: [], roles: [roleId] },
        nonce,
        enforceNonce: true,
      });
      lastSent = nonce;
    } catch (error) {
      console.error('Failed to send the CS Club meeting reminder:', error);
    } finally {
      sending = false;
    }
  }

  void checkReminder();
  setInterval(checkReminder, 15_000);
}
