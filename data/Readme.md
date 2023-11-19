# Bargaining Game Dataset - oTree Experiment

## Overview
This README file describes the dataset generated from a two-player bargaining game conducted using oTree. The experiment includes both control and treatment versions, with the latter incorporating a penalty mechanism. The dataset provides comprehensive information on participant actions and outcomes across multiple sessions of the game.

## Dataset Description
The dataset contains the following key fields:

### Participant Information
- `participant.id_in_session`: Unique identifier for each participant within a session.
- `participant.code`: A distinct code assigned to each participant.
- `participant._is_bot`: Flag indicating if the participant is a bot (0 for real participants).
- `participant.time_started_utc`: Timestamp marking the start of the participant's session.

### Game Details
- `participant._current_app_name`: Name of the current application, set as 'bargaining'.
- `participant._current_page_name`: Current page in the experiment, usually 'Results'.
- `participant.visited`: Indicates if the participant has visited this stage of the game.

### Player's Decisions and Outcomes
- `player.id_in_group`: Player's identification number within the group.
- `player.role`: Role of the player in the group.
- `player.request`: Amount requested by the player in the game.
- `player.payoff`: Payoff received by the player based on the game outcome.

### Group Dynamics
- `group.id_in_subsession`: Identifier for the group within each subsession.
- `group.total_requests`: Total amount requested by both players in a group.

### Round and Session Details
- `subsession.round_number`: Identifies the round number of the game.
- `session.code`: Unique code representing each game session.

### Treatment Application
The dataset is especially useful for analyzing the impact of the penalty mechanism in the treatment version, observable through `player.payoff` and `group.total_requests`, particularly in instances where the total requests exceed the set limit, leading to penalties.

## Usage
This dataset is ideal for research in decision-making strategies, collective bargaining dynamics, and the influence of penalty mechanisms in economic games. 

## Notes
- Data anonymization has been ensured for all participant information.
- The dataset format is conducive to statistical analysis and behavioral pattern identification.

