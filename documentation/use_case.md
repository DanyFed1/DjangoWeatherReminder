Actors:
- User
- Weather API (OpenWeatherMap)

Use Cases:
1. Register
2. Authenticate
3. Subscribe to City Weather
4. Unsubscribe from City Weather
5. Edit Subscription
6. View Subscriptions
7. Receive Weather Notification
8. Fetch Weather Data

Relationships:
- The User can Register, Authenticate, Subscribe to City Weather, Unsubscribe from City Weather, Edit Subscription, View Subscriptions, and Receive Weather Notification.
- The Third-Party Service can Authenticate, Subscribe to City Weather, Unsubscribe from City Weather, Edit Subscription, and View Subscriptions.
- The System fetches weather data from the Weather API (OpenWeatherMap).
- The Receive Weather Notification use case includes the Fetch Weather Data use case.

System Boundary:
- All use cases fall within the boundary of the DjangoWeatherReminder system. using the requirements of 