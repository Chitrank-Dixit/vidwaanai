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

### Verse 1 (Ramayan 0.621)
- **Original**: Canto LXV. The Women's Lament. 603 Then as the bards his glory sang, From beaten palms loud answer rang, As glad applauders clapped their hands, And told his deeds in distant lands. The swelling concert woke a throng Of sleeping birds to life and song: Some in the branches of the trees, Some caged in halls and galleries. Nor was the soft string music mute; The gentle whisper of the lute, And blessings sung by singers skilled The palace of the monarch filled. Eunuchs and dames of life unstained, Each in the arts of waiting trained, Drew near attentive as before, And crowded to the chamber door: These skilful when and how to shed The lustral stream o'er limb and head, Others with golden ewers stood Of water stained with sandal wood. And many a maid, pure, young, and fair, Her load of early offerings bare, Cups of the flood which all revere, And sacred things, and toilet gear. Each several thing was duly brought As rule of old observance taught, And lucky signs on each impressed Stamped it the fairest and the best. There anxious, in their long array, All waited till the shine of day: But when the king nor rose nor spoke, Doubt and alarm within them woke. Forthwith the dames, by duty led, Attendants on the monarch's bed,
- **Translation**: 

---

### Verse 2 (Ramayan 0.622)
- **Original**: 604 The Ramayana Within the royal chamber pressed To wake their master from his rest. Skilled in the lore of dreaming, they First touched the bed on which he lay. But none replied; no sound was heard,[173] Nor hand, nor head, nor body stirred. They trembled, and their dread increased, Fearing his breath of life had ceased, And bending low their heads, they shook Like the tall reeds that fringe the brook. In doubt and terror down they knelt, Looked on his face, his cold hand felt, And then the gloomy truth appeared Of all their hearts had darkly feared. Kau [alyá and Sumitrá, worn With weeping for their sons, forlorn, Woke not, but lay in slumber deep And still as death's unending sleep. Bowed down by grief, her colour fled, Her wonted lustre dull and dead, Kau [alyá shone not, like a star Obscured behind a cloudy bar. Beside the king's her couch was spread, And next was Queen Sumitrá's bed, Who shone no more with beauty's glow, Her face bedewed with tears of woe. There lapped in sleep each wearied queen, There as in sleep, the king was seen; And swift the troubling thought came o'er Their spirits that he breathed no more. At once with wailing loud and high The matrons shrieked a bitter cry, As widowed elephants bewail Their dead lord in the woody vale.
- **Translation**: 

---

### Verse 3 (Ramayan 0.623)
- **Original**: Canto LXV. The Women's Lament. 605 At the loud shriek that round them rang, Kau [alyá and Sumitrá sprang Awakened from their beds, with eyes Wide open in their first surprise. Quick to the monarch's side they came, And saw and touched his lifeless frame; One cry, O husband! forth they sent, And prostrate to the ground they went. The king of Ko[al's daughter338 there Writhed, with the dust on limb and hair Lustreless, as a star might lie Hurled downward from the glorious sky. When the king's voice in death was stilled, The women who the chamber filled Saw, like a widow elephant slain, Kau [alyá prostrate in her pain. Then all the monarch's ladies led By Queen Kaikeyí at their head, Poured forth their tears, and weeping so, Sank on the ground, consumed by woe. The cry of grief so long and loud Went up from all the royal crowd, That, doubled by the matron train, It made the palace ring again. Filled with dark fear and eager eyes, Anxiety and wild surmise; Echoing with the cries of grief Of sorrowing friends who mourned their chief, Dejected, pale with deep distress, Hurled from their height of happiness: Such was the look the palace wore Where lay the king who breathed no more. 338 Kau [alyá, daughter of the king of another Ko[al.
- **Translation**: 

---

### Verse 4 (Ramayan 0.624)
- **Original**: 606 The Ramayana Canto LXVI. The Embalming. Kau [alyá's eyes with tears o'erflowed, Weighed down by varied sorrows' load; On her dead lord her gaze she bent, Who lay like fire whose might is spent, Like the great deep with waters dry, Or like the clouded sun on high. Then on her lap she laid his head. And on Kaikeyí looked and said: “Triumphant now enjoy thy reign Without a thorn thy side to pain. Thou hast pursued thy single aim, And killed the king, O wicked dame. Far from my sight my Ráma flies, My perished lord has sought the skies. No friend, no hope my life to cheer, I cannot tread the dark path here. Who would forsake her husband, who That God to whom her love is due, And wish to live one hour, but she Whose heart no duty owns, like thee? The ravenous sees no fault: his greed Will e'en on poison blindly feed. Kaikeyí, through a hump-back maid, This royal house in death has laid. King Janak, with his queen, will hear Heart rent like me the tidings drear Of Ráma banished by the king, Urged by her impious counselling. No son has he, his age is great, And sinking with the double weight, He for his darling child will pine, And pierced with woe his life resign.
- **Translation**: 

---

### Verse 5 (Ramayan 0.625)
- **Original**: Canto LXVI. The Embalming. 607 Sprung from Videha's monarch, she A sad and lovely devotee, Roaming the wood, unmeet for woe, Will toil and trouble undergo. She in the gloomy night with fear The cries of beast and bird will hear, And trembling in her wild alarm Will cling to Ráma's sheltering arm. Ah, little knows my duteous son That I am widowed and undone— My Ráma of the lotus eye, Gone hence, gone hence, alas, to die. Now, as a living wife and true, I, e'en this day, will perish too: Around his form these arms will throw And to the fire with him will go.” Clasping her husband's lifeless clay A while the weeping votaress lay, Till chamberlains removed her thence [174] O'ercome by sorrow's violence. Then in a cask of oil they laid Him who in life the world had swayed, And finished, as the lords desired, All rites for parted souls required. The lords, all-wise, refused to burn The monarch ere his son's return; So for a while the corpse they set Embalmed in oil, and waited yet. The women heard: no doubt remained, And wildly for the king they plained. With gushing tears that drowned each eye Wildly they waved their arms on high, And each her mangling nails impressed
- **Translation**: 

---

### Verse 6 (Ramayan 0.626)
- **Original**: 608 The Ramayana Deep in her head and knee and breast: “Of Ráma reft,— who ever spake The sweetest words the heart to take, Who firmly to the truth would cling,— Why dost thou leave us, mighty King? How can the consorts thou hast left Widowed, of Raghu's son bereft, Live with our foe Kaikeyí near, The wicked queen we hate and fear? She threw away the king, her spite Drove Ráma forth and LakshmaG's might, And gentle Sítá: how will she Spare any, whosoe'er it be?” Oppressed with sorrow, tear-distained, The royal women thus complained. Like night when not a star appears, Like a sad widow drowned in tears, Ayodhyá's city, dark and dim, Reft of her lord was sad for him. When thus for woe the king to heaven had fled, And still on earth his lovely wives remained. With dying light the sun to rest had sped, And night triumphant o'er the landscape reigned. Canto LXVII. The Praise Of Kings.
- **Translation**: 

---

### Verse 7 (Ramayan 0.627)
- **Original**: Canto LXVII. The Praise Of Kings. 609 That night of sorrow passed away, And rose again the God of Day. Then all the twice-born peers of state Together met for high debate. Jáválí, lord of mighty fame. And Gautam, and Kátyáyan came, And Márkandeya's reverend age, And Vámadeva, glorious sage: Sprung from Mudgalya's seed the one, The other ancient Ka[yap's son. With lesser lords these Bráhmans each Spoke in his turn his several speech, And turning to Va[ishmha, best Of household priests him thus addressed: “The night of bitter woe has past, Which seemed a hundred years to last, Our king, in sorrow for his son, Reunion with the Five has won. His soul is where the blessed are, While Ráma roams in woods afar, And Lakshma G, bright in glorious deeds, Goes where his well-loved brother leads. And Bharat andZatrughna, they Who smite their foes in battle fray, Far in the realm of Kekaya stay, Where their maternal grandsire's care Keeps Rájagriha's city fair. Let one of old Ikshváku's race Obtain this day the sovereign's place, Or havoc and destruction straight Our kingless land will devastate. In kingless lands no thunder's voice, No lightning wreaths the heart rejoice, Nor does Parjanya's heavenly rain
- **Translation**: 

---

### Verse 8 (Ramayan 0.628)
- **Original**: 610 The Ramayana Descend upon the burning plain. Where none is king, the sower's hand Casts not the seed upon the land; The son against the father strives. And husbands fail to rule their wives. In kingless realms no princes call Their friends to meet in crowded hall; No joyful citizens resort To garden trim or sacred court. In kingless realms no Twice-born care To sacrifice with text and prayer, Nor Bráhmans, who their vows maintain, The great solemnities ordain. The joys of happier days have ceased: No gathering, festival, or feast Together calls the merry throng Delighted with the play and song. In kingless lands it ne'er is well With sons of trade who buy and sell: No men who pleasant tales repeat Delight the crowd with stories sweet. In kingless realms we ne'er behold Young maidens decked with gems and gold, Flock to the gardens blithe and gay To spend their evening hours in play. No lover in the flying car Rides with his love to woods afar. In kingless lands no wealthy swain Who keeps the herd and reaps the grain, Lies sleeping, blest with ample store, Securely near his open door. Upon the royal roads we see No tusked elephant roaming free, Of three-score years, whose head and neck
- **Translation**: 

---

### Verse 9 (Ramayan 0.629)
- **Original**: Canto LXVII. The Praise Of Kings. 611 Sweet tinkling bells of silver deck. We hear no more the glad applause When his strong bow each rival draws, No clap of hands, no eager cries That cheer each martial exercise. In kingless realms no merchant bands Who travel forth to distant lands, With precious wares their wagons load, [175] And fear no danger on the road. No sage secure in self-control, Brooding on God with mind and soul, In lonely wanderings finds his home Where'er at eve his feet may roam. In kingless realms no man is sure He holds his life and wealth secure. In kingless lands no warriors smite The foeman's host in glorious fight. In kingless lands the wise no more, Well trained in Scripture's holy lore, In shady groves and gardens meet To argue in their calm retreat. No longer, in religious fear, Do they who pious vows revere, Bring dainty cates and wreaths of flowers As offerings to the heavenly powers. No longer, bright as trees in spring, Shine forth the children of the king Resplendent in the people's eyes With aloe wood and sandal dyes. A brook where water once has been, A grove where grass no more is green, Kine with no herdsman's guiding hand— So wretched is a kingless land. The car its waving banner rears,
- **Translation**: 

---

### Verse 10 (Ramayan 0.630)
- **Original**: 612 The Ramayana Banner of fire the smoke appears: Our king, the banner of our pride, A God with Gods is glorified. In kingless lands no law is known, And none may call his wealth his own, Each preys on each from hour to hour, As fish the weaker fish devour. Then fearless, atheists overleap The bounds of right the godly keep, And when no royal powers restrain, Preëminence and lordship gain. As in the frame of man the eye Keeps watch and ward, a careful spy, The monarch in his wide domains Protects the truth, the right maintains. He is the right, the truth is he, Their hopes in him the well-born see. On him his people's lives depend, Mother is he, and sire, and friend. The world were veiled in blinding night, And none could see or know aright, Ruled there no king in any state The good and ill to separate. We will obey thy word and will As if our king were living still: As keeps his bounds the faithful sea, So we observe thy high decree. O best of Bráhmans, first in place, Our kingless land lies desolate: Some scion of Ikshváku's race Do thou as monarch consecrate.”
- **Translation**: 

---

### Verse 11 (Ramayan 0.631)
- **Original**: Canto LXVIII. The Envoys. 613 Canto LXVIII. The Envoys. Va [ishmha heard their speech and prayer, And thus addressed the concourse there, Friends, Bráhmans, counsellors, and all Assembled in the palace hall: “Ye know that Bharat, free from care, Still lives in Rájagriha339 where The father of his mother reigns: Zatrughna by his side remains. Let active envoys, good at need, Thither on fleetest horses speed, To bring the hero youths away: Why waste the time in dull delay?” Quick came from all the glad reply: “Va [ishmha, let the envoys fly!” He heard their speech, and thus renewed His charge before the multitude: “Nandan, A[ok, Siddhárth, attend, Your ears, Jayanta, Vijay, lend: Be yours, what need requires, to do: I speak these words to all of you. With coursers of the fleetest breed To Rájagriha's city speed. Then rid your bosoms of distress, And Bharat thus from me address: “The household priest and peers by us Send health to thee and greet thee thus: Come to thy father's home with haste: Thine absent time no longer waste.” 339 Rájagriha, or Girivraja was the capital of A[vapati, Bharat's maternal grandfather.
- **Translation**: 

---

### Verse 12 (Ramayan 0.632)
- **Original**: 614 The Ramayana But speak no word of Ráma fled, Tell not the prince his sire is dead, Nor to the royal youth the fate That ruins Raghu's race relate. Go quickly hence, and with you bear Fine silken vestures rich and rare, And gems and many a precious thing As gifts to Bharat and the king.” With ample stores of food supplied, Each to his home the envoys hied, Prepared, with steeds of swiftest race, To Kekaya's land340 their way to trace. They made all due provision there, And every need arranged with care, Then ordered by Va[ishmha, they Went forth with speed upon their way. Then northward of Pralamba, west Of Apartála, on they pressed, Crossing the Máliní that flowed With gentle stream athwart the road. They traversed Gangá's holy waves[176] Where she Hástinapura341 laves, Thence to Panchála342 westward fast Through Kurujángal's land343 Note. 340 The Kekayas or Kaikayas in the Punjab appear amongst the chief nations in the war of the Mahábhárata; their king being a kinsman of KrishGa. 341 Hástinapura was the capital of the kingdom of Kuru, near the modern Delhi. 342 The Panchálas occupied the upper part of the Doab. 343 “Kurujángala and its inhabitants are frequently mentioned in the Mahábhárata, as in theÁdi-parv.3789, 4337,et al.” W ILSON 'S{FNS VishGu PuráGa,Vol. II. p. 176. DR . HALL 'S{FNS
- **Translation**: 

---

### Verse 13 (Ramayan 0.633)
- **Original**: Canto LXVIII. The Envoys. 615 they passed. On, on their course the envoys held By urgency of task impelled. Quick glancing at each lucid flood And sweet lake gay with flower and bud. Beyond, they passed unwearied o'er, Where glad birds fill the flood and shore Of ZaradaG á racing fleet With heavenly water clear and sweet, Thereby a tree celestial grows Which every boon on prayer bestows: To its blest shade they humbly bent, Then to Kulingá's town they went. Then, having passed the Warrior's Wood, In Abhikála next they stood, O'er sacred Ikshumatí344 Edition. The Ikshumatí was a river in Kurukshetra. came, Their ancient kings' ancestral claim. They saw the learned Bráhmans stand, Each drinking from his hollowed hand, And through Báhíka345 journeying still They reached at length Sudáman's hill: There VishGu's footstep turned to see, Vipá[á346 viewed, andZálmalí, And many a lake and river met, Tank, pool, and pond, and rivulet. 344 “The I¾{¼±Ä¹Â of Arrian. SeeAs. Res. Vol. XV. p. 420, 421, also Indische Alterthumskunde, Vol. I. p. 602, first footnote.” W ILSON 'S{FNS VishGu PuráGa, Vol. I. p. 421. DR . HALL 'S{FNS 345 “The Báhíkas are described in the Mahábhárata, KarGa Parvan, with some detail, and comprehend the different nations of the Punjab from the Sutlej to the Indus.” W ILSON 'S{FNS VishGu PuráGa, Vol. I. p. 167. 346 The Beas, Hyphasis, or Bibasis.
- **Translation**: 

---

### Verse 14 (Ramayan 0.634)
- **Original**: 616 The Ramayana And lions saw, and tigers near, And elephants and herds of deer, And still, by prompt obedience led, Along the ample road they sped. Then when their course so swift and long, Had worn their steeds though fleet and strong, To Girivraja's splendid town They came by night, and lighted down. To please their master, and to guard The royal race, the lineal right, The envoys, spent with riding hard, To that fair city came by night.347 347 It would be lost labour to attempt to verify all the towns and streams mentioned in Cantos LXVIII and LXXII. Professor Wilson observes (VishGu PuráGa, p. 139. Dr. Hall's Edition)“States, and tribes, and cities have disap- peared, even from recollection; and some of the natural features of the country, especially the rivers, have undergone a total alteration.… Notwithstanding these impediments, however, we should be able to identify at least mountains and rivers, to a much greater extent than is now practicable, if our maps were not so miserably defective in their nomenclature. None of our surveyors or geographers have been oriental scholars. It may be doubted if any of them have been conversant with the spoken language of the country. They have, consequently, put down names at random, according to their own inaccurate appreciation of sounds carelessly, vulgarly, and corruptly uttered; and their maps of India are crowded with appellations which bear no similitude whatever either to past or present denominations. We need not wonder that we cannot discover Sanskrit names in English maps, when, in the immediate vicinity of Calcutta, Barnagore represents Baráhanagar, Dakshine[war is metamorphosed into Duckinsore, Ulubaría into Willoughbury.… There is scarcely a name in our Indian maps that does not afford proof of extreme indifference to accuracy in nomenclature, and of an incorrectness in estimating sounds, which is, in some degree, perhaps, a national defect.” For further information regarding the road from Ayodhyá to Rájagriha, see
- **Translation**: 

---

### Verse 15 (Ramayan 0.635)
- **Original**: Canto LXIX. Bharat's Dream. 617 Canto LXIX. Bharat's Dream. The night those messengers of state Had past within the city's gate, In dreams the slumbering Bharat saw A sight that chilled his soul with awe. The dream that dire events foretold Left Bharat's heart with horror cold, [177] And with consuming woes distraught, Upon his aged sire he thought. His dear companions, swift to trace The signs of anguish on his face, Drew near, his sorrow to expel, And pleasant tales began to tell. Some woke sweet music's cheering sound, And others danced in lively round. With joke and jest they strove to raise His spirits, quoting ancient plays; But Bharat still, the lofty-souled, Deaf to sweet tales his fellows told, Unmoved by music, dance, and jest, Sat silent, by his woe oppressed. To him, begirt by comrades near, Thus spoke the friend he held most dear: “Why ringed around by friends, art thou So silent and so mournful now?” “Hear thou,” thus Bharat made reply, “What chills my heart and dims mine eye. I dreamt I saw the king my sire Sink headlong in a lake of mire Down from a mountain high in air, His body soiled, and loose his hair. Additional Notes.
- **Translation**: 

---

### Verse 16 (Ramayan 0.636)
- **Original**: 618 The Ramayana Upon the miry lake he seemed To lie and welter, as I dreamed; With hollowed hands full many a draught Of oil he took, and loudly laughed. With head cast down I saw him make A meal on sesamum and cake; The oil from every member dripped, And in its clammy flood he dipped. The ocean's bed was bare and dry, The moon had fallen from the sky, And all the world lay still and dead, With whelming darkness overspread. The earth was rent and opened wide, The leafy trees were scorched, and died; I saw the seated mountains split, And wreaths of rising smoke emit. The stately beast the monarch rode His long tusks rent and splintered showed; And flames that quenched and cold had lain Blazed forth with kindled light again. I looked, and many a handsome dame, Arrayed in brown and sable came And bore about the monarch, dressed, On iron stool, in sable vest. And then the king, of virtuous mind, A blood-red wreath around him twined, Forth on an ass-drawn chariot sped, As southward still he bent his head. Then, crimson-clad, a dame appeared Who at the monarch laughed and jeered; And a she-monster, dire to view, Her hand upon his body threw. Such is the dream I dreamt by night, Which chills me yet with wild affright:
- **Translation**: 

---

### Verse 17 (Ramayan 0.637)
- **Original**: Canto LXX. Bharat's Departure. 619 Either the king or Ráma, I Or LakshmaG now must surely die. For when an ass-drawn chariot seems To bear away a man in dreams, Be sure above his funeral pyre The smoke soon rears its cloudy spire. This makes my spirit low and weak, My tongue is slow and loth to speak: My lips and throat are dry for dread, And all my soul disquieted. My lips, relaxed, can hardly speak, And chilling dread has changed my cheek I blame myself in aimless fears, And still no cause of blame appears. I dwell upon this dream of ill Whose changing scenes I viewed, And on the startling horror still My troubled thoughts will brood. Still to my soul these terrors cling, Reluctant to depart, And the strange vision of the king Still weighs upon my heart.” Canto LXX. Bharat's Departure. While thus he spoke, the envoys borne On horses faint and travel-worn Had gained the city fenced around With a deep moat's protecting bound. An audience of the king they gained, And honours from the prince obtained;
- **Translation**: 

---

### Verse 18 (Ramayan 0.638)
- **Original**: 620 The Ramayana The monarch's feet they humbly pressed, To Bharat next these words addressed: “The household priest and peers by us Send health to thee and greet thee thus: “Come to thy father's house with haste: Thine absent time no longer waste.” Receive these vestures rich and rare, These costly gems and jewels fair, And to thy uncle here present Each precious robe and ornament. These for the king and him suffice— Two hundred millions is their price— These, worth a hundred millions, be Reserved, O large-eyed Prince, for thee.” Loving his friends with heart and soul, The joyful prince received the whole, Due honour to the envoys paid, And thus in turn his answer made: “Of Da[aratha tidings tell: Is the old king my father well? Is Ráma, and is LakshmaG, he Of the high-soul, from sickness free? And she who walks where duty leads, Kau [alyá, known for gracious deeds, Mother of Ráma, loving spouse, Bound to her lord by well kept vows? And Lakshma G's mother too, the dame Sumitrá skilled in duty's claim, Who brave Zatrughna also bare, Second in age,— her health declare.[178] And she, in self-conceit most sage, With selfish heart most prone to rage, My mother, fares she well? has she
- **Translation**: 

---

### Verse 19 (Ramayan 0.639)
- **Original**: Canto LXX. Bharat's Departure. 621 Sent message or command to me?” Thus Bharat spake, the mighty-souled, And they in brief their tidings told: “All they of whom thou askest dwell, O lion lord, secure and well: Thine all the smiles of fortune are: Make ready; let them yoke the car.” Thus by the royal envoys pressed, Bharat again the band addressed: “I go with you: no long delay, A single hour I bid you stay.” Thus Bharat, son of him who swayed Ayodhyás realm, his answer made, And then bespoke, his heart to please, His mother's sire in words like these: “I go to see my father, King, Urged by the envoys' summoning; And when thy soul desires to see Thy grandson, will return to thee.” The king his grandsire kissed his head, And in reply to Bharat said: “Go forth, dear child: how blest is she, The mother of a son like thee! Greet well thy sire, thy mother greet, O thou whose arms the foe defeat; The household priest, and all the rest Amid the Twice-born chief and best; And Ráma and brave LakshmaG, who Shoot the long shaft with aim so true.”
- **Translation**: 

---

### Verse 20 (Ramayan 0.640)
- **Original**: 622 The Ramayana To him the king high honour showed, And store of wealth and gifts bestowed, The choicest elephants to ride, And skins and blankets deftly dyed, A thousand strings of golden beads, And sixteen hundred mettled steeds: And boundless wealth before him piled Gave Kekaya to Kaikeyí's child. And men of counsel, good and tried, On whose firm truth he aye relied, King A[vapati gave with speed Prince Bharat on his way to lead. And noble elephants, strong and young, From sires of Indra[ira sprung, And others tall and fair to view Of great Airávat's lineage true: And well yoked asses fleet of limb The prince his uncle gave to him. And dogs within the palace bred, Of body vast and massive head, With mighty fangs for battle, brave, The tiger's match in strength, he gave. Yet Bharat's bosom hardly glowed To see the wealth the king bestowed; For he would speed that hour away, Such care upon his bosom lay: Those eager envoys urged him thence, And that sad vision's influence. He left his court-yard, crowded then With elephants and steeds and men, And, peerless in immortal fame, To the great royal street he came. He saw, as farther still he went, The inner rooms most excellent,
- **Translation**: 

---

