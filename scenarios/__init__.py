from scenarios.following_dialogue import FollowingDialogueScenario
from scenarios.following_dialogue_parse import FollowingDialogueParseScenario
from scenarios.following_dialogue_unsubscribe import \
    FollowingDialogueUnsubscribeScenario
from scenarios.main_page import MainPageScenario
from scenarios.login import LoginScenario
from scenarios.profile_page import ProfilePageScenario


scenarios_list = [
    MainPageScenario,  # Go to main page
    LoginScenario,  # Login
    ProfilePageScenario,  # Go to profile page
    FollowingDialogueScenario,  # Show following dialogue
    FollowingDialogueParseScenario,  # Parse username from following dialogue
    FollowingDialogueUnsubscribeScenario  # Unsubscribe followings
]
