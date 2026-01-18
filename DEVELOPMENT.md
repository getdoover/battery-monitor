# Battery Monitor

This application allows you to monitor the state of a battery pack in 12V, 24 or 48V configurations. 

It exposes config that allows you to set the pack size, and then sets some reasonable values for "Low", "OK", "Charging" and "High".


### Prerequisites

- Docker and Docker Compose installed
- Python 3.11 or later (if running locally)
- Pipenv for managing Python dependencies

### Running Locally

1. Run the application:

```bash
doover app run
```

## Simulators

The `simulator/` directory contains tools for simulating application behavior. For example:

- `app_config.json`: Sample configuration file for the app.
- `docker-compose.yml`: Defines services for running the application.

You can find a sample simulator in the `simulator/sample/` directory. While it is fairly bare-bones, it shows
positioning of the simulator in the application structure, and how to start the simulator alongside your application.

## Testing

Run the tests using the following command:

```bash
pytest tests/
```

## Deployment

The `deployment/` directory contains deployment configurations, including a `docker-compose.yml` file for orchestrating
services.

## Customization

To create your own Doover application:

1. Modify the application logic in the appropriate directory.
2. Update the simulator and test configurations as needed.
3. Adjust deployment configurations to suit your requirements.
