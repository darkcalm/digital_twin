# Task List: MCP Server for Digital Twin Simulation

## Relevant Files

- `main.py` - Main FastAPI application that will be modified to integrate MCP server
- `simulation.py` - Existing plant simulation module that needs to be adapted for MCP
- `robot_simulation.py` - New module for robot simulation and storage functionality
- `mcp_server.py` - New module for MCP server implementation
- `mcp_config.py` - Configuration module for MCP server settings
- `requirements.txt` - Dependencies file to be updated with MCP SDK
- `tests/test_mcp_server.py` - Unit tests for MCP server functionality
- `tests/test_robot_simulation.py` - Unit tests for robot simulation
- `data/plant_history.json` - File for storing plant state history (created by robot)

### Notes

- Unit tests should be placed alongside the code files they are testing
- The MCP server implementation should follow the official Python SDK documentation
- File-based storage will be used for the robot's store action in this phase
- Existing plant simulation logic should be preserved while adding MCP functionality

## Tasks

- [x] 1.0 Set up MCP Server Infrastructure
  - [x] 1.1 Install and configure MCP Python SDK
  - [x] 1.2 Create basic MCP server structure in `mcp_server.py`
  - [x] 1.3 Set up MCP server configuration and initialization
  - [x] 1.4 Update `requirements.txt` with necessary dependencies
  - [x] 1.5 Create basic test structure for MCP server

- [ ] 2.0 Implement Plant Entity MCP Interface
  - [ ] 2.1 Create MCP tool definition for `set_plant_setpoint`
  - [ ] 2.2 Create MCP data resource definition for `get_plant_state`
  - [ ] 2.3 Modify `simulation.py` to expose state through MCP interface
  - [ ] 2.4 Implement validation for setpoint values (0 to 1)
  - [ ] 2.5 Add unit tests for plant MCP interface

- [ ] 3.0 Create Robot Entity Simulation
  - [ ] 3.1 Create `robot_simulation.py` with basic robot structure
  - [ ] 3.2 Implement robot initialization and state management
  - [ ] 3.3 Create interface for robot to access plant state
  - [ ] 3.4 Add unit tests for robot simulation

- [ ] 4.0 Implement Robot's Store Action
  - [ ] 4.1 Create file-based storage system for plant state
  - [ ] 4.2 Implement store action in robot simulation
  - [ ] 4.3 Add timestamp to stored plant state data
  - [ ] 4.4 Create data directory structure for storage
  - [ ] 4.5 Add unit tests for store action

- [ ] 5.0 Integrate and Test MCP Server
  - [ ] 5.1 Modify `main.py` to initialize both plant and robot simulations
  - [ ] 5.2 Integrate MCP server with FastAPI application
  - [ ] 5.3 Test concurrent client connections
  - [ ] 5.4 Verify plant state persistence through robot
  - [ ] 5.5 Create integration tests for full system 