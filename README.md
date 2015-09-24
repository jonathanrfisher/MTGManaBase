# MTGManaBase
Engine for determining optimal BFZ Standard mana base for a given set of 36 cards.

A standard deck will consist of 60 cards for the purpose
of testing.

We will first consider only 24 land decks for the purpose
of testing.

The composition of the casting costs for the remaining
36 cards will vary as designed in the test data and
this will be the primary driver for test results.

Our goal will be to find the optimal mana base for
each given deck where the deck is defined to be
the collection of 36 spells and their corresponding
mana costs.

A mana base will be considered optimal if it gives
the greatest oppurtunity to be able to cast each spell
in the deck on the appropriate turn.  We will not
at first consider the ability to cast two spells per turn
and we will not consider casting lower cost spells on
higher turns.

A deck will be represented by an array of casting costs
for each converted mana cost from 1-7.  We will not
consider manabases for spells greater than 7 for this
exercise since color availability becomes less relavant
as converted mana costs increase and most spells costing
8+ tend to be colorless in current standard (BFZ).

The importance or 'weight' for being able to cast a spell
on the appropriate turn will be directly proportional to
it's ranking in the converted mana costs where lower costs
are ranked higher.  An optimal manabase will then be the
manabase which scores greatest based on these rankings.

We will not be considering % chances to draw particular
color combinations from our manabase since the highest
ranked manabase should be expected to also have the
greatest percent chance to draw the appropriate color
combinations on the corresponding turns.  We will however
have to consider whether a land will be tapped or untapped
and the appropriate sequencing.

We must consider how our need to play tapped lands in order
to cast higher casting cost cards effects our ability
to cast our lower costed cards.  Therefore we must accrue
some penalty for requiring tapped lands IF those lands
would also have been needed to cast lower costed spells.

Life total consideration due to excessive fetchlands will
NOT be considered for the purpose of this test.
