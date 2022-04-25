# Initialize dictionary that stores location directions, items, and descriptions
story_map = {
    'Central Elevator': {
        'Item': '',
        'Comment': "The elevator is perfectly intact and doesn't show the \ndevastation occurring elsewhere on the "
                   "station.",
        'North': 'Hydrogarden', 'East': 'Central Command', 'West': 'Mess Room'},
    'Hydrogarden': {
        'Item': 'CO2 Tank',
        'Comment': "Flowering plants hang densely in the moist air.",
        'South': 'Central Elevator'},
    'Maintenance Room': {
        'Item': 'Air Lock SDS',
        'Comment': "The room is densely packed with tools and smells like \nhydraulic oil.",
        'South': 'Central Command', 'East': 'Air Lock'},
    'Central Command': {
        'Item': 'Sheet of Access Codes',
        'Comment': 'The room is in panicked disarray. There has clearly been a \nfight here. Blood streaks most '
                   'surfaces.',
        'North': 'Maintenance Room', 'West': 'Central Elevator', 'South': 'Engineering Wing'},
    'Engineering Wing': {
        'Item': 'Air Hose Adapter',
        'Comment': 'Filled with computers and important instruments, mostly intact.',
        'North': 'Central Command', 'West': 'Space Walk'},
    'Space Walk': {
        'Item': 'Space Suit',
        'Comment': "One of the slotted suits is missing - did someone try to escape \nthe organism by fleeing into "
                   "space?",
        'East': 'Engineering Wing'},
    'Mess Room': {
        'Item': 'Plasma Knife',
        'Comment': 'There are signs of an evening meal, long abandoned.',
        'West': 'Barracks', 'East': 'Central Elevator'},
    'Barracks': {
        'Item': 'Butane Lighter',
        'Comment': 'The orderly bunks and personal storages are well kempt.',
        'North': 'Medical Bay', 'East': 'Mess Room'},
    'Medical Bay': {
        'Item': 'Roll of Bandages',
        'Comment': 'Most of the cabinets are open, supplies pilfered.',
        'South': 'Barracks'}
}