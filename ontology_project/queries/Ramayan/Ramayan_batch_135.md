# Manual Entity Extraction Prompt

Please extract entities (Deities, Concepts, Characters, Locations, Events) and their relationships from the following verses.
Return the output in strict JSON format.

## Valid Schema
- **Entity Types**: Deity, Concept, Character, Place, Event, Text
- **Relationship Types**: MENTIONS, IS_AVATAR_OF, RELATED_TO, LOCATED_AT, PARTICIPATED_IN

## JSON Format
```json
{
  "entities": [
    {"name": "EntityName", "type": "Type", "attributes": {"description": "..."}}
  ],
  "relationships": [
    {"from": "Entity1", "to": "Entity2", "type": "RELATION", "attributes": {"context": "..."}}
  ]
}
```

## Verses to Analyze

### Verse 1 (Ramayana 0.726)
- **Original**: 708 The Ramayana Afar umbrageous woods arise Like darksome clouds that veil the skies. Now tread these mountain-beasts of mine On Chitrakúma's fair incline. The trees their rain of blossoms shed On table-lands beneath them spread, As from black clouds the floods descend When the hot days of summer end. Zatrughna, look, the mountain see Where heavenly minstrels wander free,[202] And horses browse beneath the steep, Countless as monsters in the deep. Scared by my host the mountain deer Starting with tempest speed appear Like the long lines of cloud that fly In autumn through the windy sky. See, every warrior shows his head With fragrant blooms engarlanded; All look like southern soldiers who Lift up their shields of azure hue. This lonely wood beneath the hill, That was so dark and drear and still, Covered with men in endless streams Now like Ayodhyá's city seems. The dust which countless hoofs excite Obscures the sky and veils the light; But see, swift winds those clouds dispel As if they strove to please me well. See, guided in their swift career By many a skilful charioteer, Those cars by fleetest coursers drawn Race onward over glade and lawn. Look, startled as the host comes near The lovely peacocks fly in fear,
- **Translation**: 

---

### Verse 2 (Ramayana 0.727)
- **Original**: Canto XCIII. Chitrakúta In Sight. 709 Gorgeous as if the fairest blooms Of earth had glorified their plumes. Look where the sheltering covert shows The trooping deer, both bucks and does, That occupy in countless herds This mountain populous with birds. Most lovely to my mind appears This place which every charm endears: Fair as the road where tread the Blest; Here holy hermits take their rest. Then let the army onward press And duly search each green recess For the two lion-lords, till we Ráma once more and LakshmaG see.” Thus Bharat spoke: and hero bands Of men with weapons in their hands Entered the tangled forest: then A spire of smoke appeared in ken. Soon as they saw the rising smoke To Bharat they returned and spoke: “No fire where men are not: 'tis clear That Raghu's sons are dwelling here. Or if not here those heroes dwell Whose mighty arms their foeman quell, Still other hermits here must be Like Ráma, true and good as he.” His ears attentive Bharat lent To their resistless argument, Then to his troops the chief who broke His foe's embattled armies spoke: “Here let the troops in silence stay; One step beyond they must not stray.
- **Translation**: 

---

### Verse 3 (Ramayana 0.728)
- **Original**: 710 The Ramayana Come Dhrishmi and Sumantra, you With me alone the path pursue.” Their leader's speech the warriors heard, And from his place no soldier stirred, And Bharat bent his eager eyes Where curling smoke was seen to rise. The host his order well obeyed, And halting there in silence stayed Watching where from the thicket's shade They saw the smoke appear. And joy through all the army ran, “Soon shall we meet,” thought every man, “The prince we hold so dear.” Canto XCIV. Chitrakúta. There long the son of Raghu dwelt And love for hill and wood he felt. Then his Videhan spouse to please And his own heart of woe to ease, Like some Immortal— Indra so Might Swarga's charms toZachí show— Drew her sweet eyes to each delight Of Chitrakúma's lovely height: “Though reft of power and kingly sway, Though friends and home are far away, I cannot mourn my altered lot, Enamoured of this charming spot. Look, darling, on this noble hill Which sweet birds with their music fill,
- **Translation**: 

---

### Verse 4 (Ramayana 0.729)
- **Original**: Canto XCIV. Chitrakúta. 711 Bright with a thousand metal dyes His lofty summits cleave the skies. See, there a silvery sheen is spread, And there like blood the rocks are red. There shows a streak of emerald green, And pink and yellow glow between. There where the higher peaks ascend, Crystal and flowers and topaz blend, And others flash their light afar Like mercury or some fair star: With such a store of metals dyed The king of hills is glorified. There through the wild birds' populous home The harmless bear and tiger roam: Hyænas range the woody slopes With herds of deer and antelopes. See, love, the trees that clothe his side All lovely in their summer pride, In richest wealth of leaves arrayed, With flower and fruit and light and shade, Look where the young Rose-apple glows; What loaded boughs the Mango shows; See, waving in the western wind The light leaves of the Tamarind, And mark that giant Peepul through The feathery clump of tall bamboo.369 [203] Look, on the level lands above, Delighting in successful love 369 These ten lines are a substitution for, and not a translation of the text which Carey and Marshman thus render:“This mountain adorned with mango, jumboo, usuna, lodhra, piala, punusa, dhava, unkotha, bhuvya, tinisha, vilwa, tindooka, bamboo, kashmaree, urista, uruna, madhooka, tilaka, vuduree, am- luka, nipa, vetra, dhunwuna, veejaka, and other trees affording flowers, and fruits, and the most delightful shade, how charming does it appear!”
- **Translation**: 

---

### Verse 5 (Ramayana 0.730)
- **Original**: 712 The Ramayana In sweet enjoyment many a pair Of heavenly minstrels revels there, While overhanging boughs support Their swords and mantles as they sport: Then see that pleasant shelter where Play the bright Daughters of the Air.370 The mountain seems with bright cascade And sweet rill bursting from the shade, Like some majestic elephant o'er Whose burning head the torrents pour. Where breathes the man who would not feel Delicious languor o'er him steal, As the young morning breeze that springs From the cool cave with balmy wings, Breathes round him laden with the scent Of bud and blossom dew-besprent? If many autumns here I spent With thee, my darling innocent, And Lakshma G, I should never know The torture of the fires of woe, This varied scene so charms my sight, This mount so fills me with delight, Where flowers in wild profusion spring, And ripe fruits glow and sweet birds sing. My beauteous one, a double good Springs from my dwelling in the wood: Loosed is the bond my sire that tied, And Bharat too is gratified. My darling, dost thou feel with me Delight from every charm we see, Of which the mind and every sense Feel the enchanting influence? 370 Vidyadharis, Spirits of Air, sylphs.
- **Translation**: 

---

### Verse 6 (Ramayana 0.731)
- **Original**: Canto XCIV. Chitrakúta. 713 My fathers who have passed away, The royal saints, were wont to say, That life in woodland shades like this Secures a king immortal bliss. See, round the hill at random thrown, Huge masses lie of rugged stone Of every shape and many a hue, Yellow and white and red and blue. But all is fairer still by night: Each rock reflects a softer light, When the whole mount from foot to crest In robes of lambent flame is dressed; When from a million herbs a blaze Of their own luminous glory plays, And clothed in fire each deep ravine, Each pinnacle and crag is seen. Some parts the look of mansions wear, And others are as gardens fair, While others seem a massive block Of solid undivided rock. Behold those pleasant beds o'erlaid With lotus leaves, for lovers made, Where mountain birch and costus throw Cool shadows on the pair below. See where the lovers in their play Have cast their flowery wreaths away, And fruit and lotus buds that crowned Their brows lie trodden on the ground. North Kuru's realm is fair to see, Vasvaukasárá,371 Naliní,372 But rich in fruit and blossom still 371 A lake attached either to Amarávatí the residence of Indra, or Alaká that of Kuvera. 372 The Ganges of heaven.
- **Translation**: 

---

### Verse 7 (Ramayana 0.732)
- **Original**: 714 The Ramayana More fair is Chitrakúma's hill. Here shall the years appointed glide With thee, my beauty, by my side, And Lakshma G ever near; Here shall I live in all delight, Make my ancestral fame more bright, Tread in their path who walk aright, And to my oath adhere.” Canto XCV. Mandákiní. Then Ráma, like the lotus eyed, Descended from the mountain side, And to the Maithil lady showed The lovely stream that softly flowed. And thus Ayodhyá's lord addressed His bride, of dames the loveliest, Child of Videha's king, her face Bright with the fair moon's tender grace: “How sweetly glides, O darling, look, Mandákiní's delightful brook, Adorned with islets, blossoms gay, And sárases and swans at play![204] The trees with which her banks are lined Show flowers and fruit of every kind: The match in radiant sheen is she Of King Kuvera's Naliní.373 My heart exults with pleasure new The shelving band and ford to view, 373 Naliní, as here, may be the name of any lake covered with lotuses.
- **Translation**: 

---

### Verse 8 (Ramayana 0.733)
- **Original**: Canto XCV. Mandákiní. 715 Where gathering herds of thirsty deer Disturb the wave that ran so clear. Now look, those holy hermits mark In skins of deer and coats of bark; With twisted coils of matted hair, The reverend men are bathing there, And as they lift their arms on high The Lord of Day they glorify: These best of saints, my large-eyed spouse, Are constant to their sacred vows. The mountain dances while the trees Bend their proud summits to the breeze, And scatter many a flower and bud From branches that o'erhang the flood. There flows the stream like lucid pearl, Round islets here the currents whirl, And perfect saints from middle air Are flocking to the waters there. See, there lie flowers in many a heap From boughs the whistling breezes sweep, And others wafted by the gale Down the swift current dance and sail. Now see that pair of wild-fowl rise, Exulting with their joyful cries: Hark, darling, wafted from afar How soft their pleasant voices are. To gaze on Chitrakúma's hill, To look upon this lovely rill, To bend mine eyes on thee, dear wife, Is sweeter than my city life. Come, bathe we in the pleasant rill Whose dancing waves are never still, Stirred by those beings pure from sin, The sanctities who bathe therein:
- **Translation**: 

---

### Verse 9 (Ramayana 0.734)
- **Original**: 716 The Ramayana Come, dearest, to the stream descend, Approach her as a darling friend, And dip thee in the silver flood Which lotuses and lilies stud. Let this fair hill Ayodhyá seem, Its silvan things her people deem, And let these waters as they flow Our own beloved Sarjú show. How blest, mine own dear love, am I; Thou, fond and true, art ever nigh, And duteous, faithful LakshmaG stays Beside me, and my word obeys. Here every day I bathe me thrice, Fruit, honey, roots for food suffice, And ne'er my thoughts with longing stray To distant home or royal sway. For who this charming brook can see Where herds of roedeer wander free, And on the flowery-wooded brink Apes, elephants, and lions drink, Nor feel all sorrow fly?” Thus eloquently spoke the pride Of Raghu's children to his bride, And wandered happy by her side Where Chitrakúma azure-dyed Uprears his peaks on high. Canto XCVI. The Magic Shaft.374 374 This canto is allowed, by Indian commentators, to be an interpolation. It cannot be the work of Válmíki.
- **Translation**: 

---

### Verse 10 (Ramayana 0.735)
- **Original**: Canto XCVI. The Magic Shaft. 717 Thus Ráma showed to Janak's child The varied beauties of the wild, The hill, the brook and each fair spot, Then turned to seek their leafy cot. North of the mountain Ráma found A cavern in the sloping ground, Charming to view, its floor was strown With many a mass of ore and stone, In secret shadow far retired Where gay birds sang with joy inspired, And trees their graceful branches swayed With loads of blossom downward weighed. Soon as he saw the cave which took Each living heart and chained the look, Thus Ráma spoke to Sítá who Gazed wondering on the silvan view: “Does this fair cave beneath the height, Videhan lady, charm thy sight? Then let us resting here a while The languor of the way beguile. That block of stone so smooth and square Was set for thee to rest on there, And like a thriving Ke[ar tree This flowery shrub o'ershadows thee.” Thus Ráma spoke, and Janak's child, By nature ever soft and mild, In tender words which love betrayed Her answer to the hero made: “O pride of Raghu's children, still My pleasure is to do thy will. Enough for me thy wish to know: Far hast thou wandered to and fro.”
- **Translation**: 

---

### Verse 11 (Ramayana 0.736)
- **Original**: 718 The Ramayana Thus Sítá spake in gentle tone, And went obedient to the stone, Of perfect face and faultless limb Prepared to rest a while with him. And Ráma, as she thus replied, Turned to his spouse again and cried: “Thou seest, love, this flowery shade For silvan creatures' pleasure made, How the gum streams from trees and plants Torn by the tusks of elephants![205] Through all the forest clear and high Resounds the shrill cicala's cry. Hark how the kite above us moans, And calls her young in piteous tones; So may my hapless mother be Still mourning in her home for me. There mounted on that lofty Sál The loud Bhringráj375 repeats his call: How sweetly now he tunes his throat Responsive to the Koïl's note. Or else the bird that now has sung May be himself the Koïl's young, Linked with such winning sweetness are The notes he pours irregular. See, round the blooming Mango clings That creeper with her tender rings, So in thy love, when none is near, Thine arms are thrown round me, my dear.” Thus in his joy he cried; and she, Sweet speaker, on her lover's knee, Of faultless limb and perfect face, Grew closer to her lord's embrace. 375 A fine bird with a strong, sweet note, and great imitative powers.
- **Translation**: 

---

### Verse 12 (Ramayana 0.737)
- **Original**: Canto XCVI. The Magic Shaft. 719 Reclining in her husband's arms, A goddess in her wealth of charms, She filled his loving breast anew With mighty joy that thrilled him through. His finger on the rock he laid, Which veins of sanguine ore displayed, And painted o'er his darling's eyes The holy sign in mineral dyes. Bright on her brow the metal lay Like the young sun's first gleaming ray, And showed her in her beauty fair As the soft light of morning's air. Then from the Ke[ar's laden tree He picked fair blossoms in his glee, And as he decked each lovely tress, His heart o'erflowed with happiness. So resting on that rocky seat A while they spent in pastime sweet, Then onward neath the shady boughs Went Ráma with his Maithil spouse. She roaming in the forest shade Where every kind of creature strayed Observed a monkey wandering near, And clung to Ráma's arm in fear. The hero Ráma fondly laced His mighty arms around her waist, Consoled his beauty in her dread, And scared the Monkey till he fled. That holy mark of sanguine ore That gleamed on Sítá's brow before, Shone by that close embrace impressed Upon the hero's ample chest. Then Sítá, when the beast who led The monkey troop, afar had fled,
- **Translation**: 

---

### Verse 13 (Ramayana 0.738)
- **Original**: 720 The Ramayana Laughed loudly in light-hearted glee That mark on Ráma's chest to see. A clump of bright A[okas fired The forest in their bloom attired: The restless blossoms as they gleamed A host of threatening monkeys seemed. Then Sítá thus to Ráma cried, As longingly the flowers she eyed: “Pride of thy race, now let us go Where those A[oka blossoms grow.” He on his darling's pleasure bent With his fair goddess thither went And roamed delighted through the wood Where blossoming A[okas stood, As Ziva with Queen Umá roves Through Himaván's majestic groves. Bright with purpureal glow the pair Of happy lovers sported there, And each upon the other set A flower-inwoven coronet. There many a crown and chain they wove Of blooms from that A[oka grove, And in their graceful sport the two Fresh beauty o'er the mountain threw. The lover let his love survey Each pleasant spot that round them lay, Then turned they to their green retreat Where all was garnished, gay, and neat. By brotherly affection led, Sumitrá's son to meet them sped, And showed the labours of the day Done while his brother was away. There lay ten black-deer duly slain With arrows pure of poison stain,
- **Translation**: 

---

### Verse 14 (Ramayana 0.739)
- **Original**: Canto XCVI. The Magic Shaft. 721 Piled in a mighty heap to dry, With many another carcass nigh. And Lakshma G's brother saw, o'erjoyed, The work that had his hands employed, Then to his consort thus he cried: “Now be the general gifts supplied.” Then Sítá, fairest beauty, placed The food for living things to taste, And set before the brothers meat And honey that the pair might eat. They ate the meal her hands supplied, Their lips with water purified: Then Janak's daughter sat at last And duly made her own repast. The other venison, to be dried, Piled up in heaps was set aside, And Ráma told his wife to stay And drive the flocking crows away. Her husband saw her much distressed By one more bold than all the rest, Whose wings where'er he chose could fly, Now pierce the earth, now roam the sky. Then Ráma laughed to see her stirred To anger by the plaguing bird: Proud of his love the beauteous dame With burning rage was all aflame. Now here, now there, again, again She chased the crow, but all in vain, Enraging her, so quick to strike [206] With beak and wing and claw alike: Then how the proud lip quivered, how The dark frown marked her angry brow! When Ráma saw her cheek aglow With passion, he rebuked the crow.
- **Translation**: 

---

### Verse 15 (Ramayana 0.740)
- **Original**: 722 The Ramayana But bold in impudence the bird, With no respect for Ráma's word, Fearless again at Sítá flew: Then Ráma's wrath to fury grew. The hero of the mighty arm Spoke o'er a shaft the mystic charm, Laid the dire weapon on his bow And launched it at the shameless crow. The bird, empowered by Gods to spring Through earth itself on rapid wing, Through the three worlds in terror fled Still followed by that arrow dread. Where'er he flew, now here now there, A cloud of weapons filled the air. Back to the high-souled prince he fled And bent at Ráma's feet his head, And then, as Sítá looked, began His speech in accents of a man: “O pardon, and for pity's sake Spare, Ráma, spare my life to take! Where'er I turn, where'er I flee, No shelter from this shaft I see.” The chieftain heard the crow entreat Helpless and prostrate at his feet, And while soft pity moved his breast, With wisest speech the bird addressed: “I took the troubled Sítá's part, And furious anger filled my heart. Then on the string my arrow lay Charmed with a spell thy life to slay. Thou seekest now my feet, to crave Forgiveness and thy life to save. So shall thy prayer have due respect:
- **Translation**: 

---

### Verse 16 (Ramayana 0.741)
- **Original**: Canto XCVII. Lakshman's Anger. 723 The suppliant I must still protect. But ne'er in vain this dart may flee; Yield for thy life a part of thee, What portion of thy body, say, Shall this mine arrow rend away? Thus far, O bird, thus far alone On thee my pity may be shown. Forfeit a part thy life to buy: 'Tis better so to live than die.” Thus Ráma spoke: the bird of air Pondered his speech with anxious care, And wisely deemed it good to give One of his eyes that he might live. To Raghu's son he made reply: “O Ráma, I will yield an eye. So let me in thy grace confide And live hereafter single-eyed.” Then Ráma charged the shaft, and lo, Full in the eye it smote the crow. And the Videhan lady gazed Upon the ruined eye amazed. The crow to Ráma humbly bent, Then where his fancy led he went. Ráma with LakshmaG by his side With needful work was occupied. Canto XCVII. Lakshman's Anger.
- **Translation**: 

---

### Verse 17 (Ramayana 0.742)
- **Original**: 724 The Ramayana Thus Ráma showed his love the rill Whose waters ran beneath the hill, Then resting on his mountain seat Refreshed her with the choicest meat. So there reposed the happy two: Then Bharat's army nearer drew: Rose to the skies a dusty cloud, The sound of trampling feet was loud. The swelling roar of marching men Drove the roused tiger from his den, And scared amain the serpent race Flying to hole and hiding-place. The herds of deer in terror fled, The air was filled with birds o'erhead, The bear began to leave his tree, The monkey to the cave to flee. Wild elephants were all amazed As though the wood around them blazed. The lion oped his ponderous jaw, The buffalo looked round in awe. The prince, who heard the deafening sound, And saw the silvan creatures round Fly wildly startled from their rest, The glorious LakshmaG thus addressed: “Sumitrá's noble son most dear, Hark, LakshmaG, what a roar I hear, The tumult of a coming crowd, Appalling, deafening, deep, and loud! The din that yet more fearful grows Scares elephants and buffaloes, Or frightened by the lions, deer Are flying through the wood in fear. I fain would know who seeks this place Comes prince or monarch for the chase?
- **Translation**: 

---

### Verse 18 (Ramayana 0.743)
- **Original**: Canto XCVII. Lakshman's Anger. 725 Or does some mighty beast of prey Frighten the silvan herds away? 'Tis hard to reach this mountain height, Yea, e'en for birds in airy flight. Then fain, O LakshmaG, would I know What cause disturbs the forest so.” Lakshma G in haste, the wood to view, Climbed a high Sál that near him grew, The forest all around he eyed, First gazing on the eastern side. Then northward when his eyes he bent He saw a mighty armament Of elephants, and cars, and horse, And men on foot, a mingled force, And banners waving in the breeze, And spoke to Ráma words like these: “Quick, quick, my lord, put out the fire, Let Sítá to the cave retire. [207] Thy coat of mail around thee throw, Prepare thine arrows and thy bow.” In eager haste thus LakshmaG cried, And Ráma, lion lord, replied: “Still closer be the army scanned, And say who leads the warlike band.” Lakshma G his answer thus returned, As furious rage within him burned, Exciting him like kindled fire To scorch the army in his ire: “'Tis Bharat: he has made the throne By consecrating rites his own: To gain the whole dominion thus He comes in arms to slaughter us.
- **Translation**: 

---

### Verse 19 (Ramayana 0.744)
- **Original**: 726 The Ramayana I mark tree-high upon his car His flagstaff of the Kovidár,376 I see his glittering banner glance, I see his chivalry advance: I see his eager warriors shine On elephants in lengthened line. Now grasp we each the shafts and bow, And higher up the mountain go. Or in this place, O hero, stand With weapons in each ready hand. Perhaps beneath our might may fall This leader of the standard tall, And Bharat I this day may see Who brought this mighty woe on thee, Sítá, and me, who drove away My brother from the royal sway. Bharat our foe at length is nigh, And by this hand shall surely die: Brother, I see no sin at all If Bharat by my weapon fall. No fault is his who slays the foe Whose hand was first to strike the blow: With Bharat now the crime begins Who against thee and duty sins. The queen athirst for royal sway Will see her darling son to-day Fall by this hand, like some fair tree Struck by an elephant, slain by me. Kaikeyí's self shall perish too With kith and kin and retinue, And earth by my avenging deed Shall from this mass of sin be freed. 376 Bauhinea variegata, a species of ebony.
- **Translation**: 

---

### Verse 20 (Ramayana 0.745)
- **Original**: Canto XCVIII. Lakshman Calmed. 727 This day my wrath, too long restrained, Shall fall upon the foe, unchained, Mad as the kindled flame that speeds Destroying through the grass and reeds. This day mine arrows keen and fierce The bodies of the foe shall pierce: The woods on Chitrakúma's side Shall run with torrents crimson-dyed. The wandering beasts of prey shall feed On heart-cleft elephant and steed, And drag to mountain caves away The bodies that my arrows slay. Doubt not that Bharat and his train Shall in this mighty wood be slain: So shall I pay the debt my bow And these my deadly arrows owe.” Canto XCVIII. Lakshman Calmed. Then Ráma nobly calm allayed The wrath that LakshmaG's bosom swayed: “What need have we the sword to wield, To bend the bow or lift the shield, If Bharat brave, and wise, and good, Himself has sought this sheltering wood? I sware my father's will to do, And if I now my brother slew What gain in kingship should I find, Despised and scorned by all mankind? Believe me, e'en as I would shrink From poisoned meat or deadly drink,
- **Translation**: 

---

