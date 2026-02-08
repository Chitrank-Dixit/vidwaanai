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

### Verse 1 (Ramayana 0.626)
- **Original**: 608 The Ramayana Deep in her head and knee and breast: “Of Ráma reft,— who ever spake The sweetest words the heart to take, Who firmly to the truth would cling,— Why dost thou leave us, mighty King? How can the consorts thou hast left Widowed, of Raghu's son bereft, Live with our foe Kaikeyí near, The wicked queen we hate and fear? She threw away the king, her spite Drove Ráma forth and LakshmaG's might, And gentle Sítá: how will she Spare any, whosoe'er it be?” Oppressed with sorrow, tear-distained, The royal women thus complained. Like night when not a star appears, Like a sad widow drowned in tears, Ayodhyá's city, dark and dim, Reft of her lord was sad for him. When thus for woe the king to heaven had fled, And still on earth his lovely wives remained. With dying light the sun to rest had sped, And night triumphant o'er the landscape reigned. Canto LXVII. The Praise Of Kings.
- **Translation**: 

---

### Verse 2 (Ramayana 0.627)
- **Original**: Canto LXVII. The Praise Of Kings. 609 That night of sorrow passed away, And rose again the God of Day. Then all the twice-born peers of state Together met for high debate. Jáválí, lord of mighty fame. And Gautam, and Kátyáyan came, And Márkandeya's reverend age, And Vámadeva, glorious sage: Sprung from Mudgalya's seed the one, The other ancient Ka[yap's son. With lesser lords these Bráhmans each Spoke in his turn his several speech, And turning to Va[ishmha, best Of household priests him thus addressed: “The night of bitter woe has past, Which seemed a hundred years to last, Our king, in sorrow for his son, Reunion with the Five has won. His soul is where the blessed are, While Ráma roams in woods afar, And Lakshma G, bright in glorious deeds, Goes where his well-loved brother leads. And Bharat andZatrughna, they Who smite their foes in battle fray, Far in the realm of Kekaya stay, Where their maternal grandsire's care Keeps Rájagriha's city fair. Let one of old Ikshváku's race Obtain this day the sovereign's place, Or havoc and destruction straight Our kingless land will devastate. In kingless lands no thunder's voice, No lightning wreaths the heart rejoice, Nor does Parjanya's heavenly rain
- **Translation**: 

---

### Verse 3 (Ramayana 0.628)
- **Original**: 610 The Ramayana Descend upon the burning plain. Where none is king, the sower's hand Casts not the seed upon the land; The son against the father strives. And husbands fail to rule their wives. In kingless realms no princes call Their friends to meet in crowded hall; No joyful citizens resort To garden trim or sacred court. In kingless realms no Twice-born care To sacrifice with text and prayer, Nor Bráhmans, who their vows maintain, The great solemnities ordain. The joys of happier days have ceased: No gathering, festival, or feast Together calls the merry throng Delighted with the play and song. In kingless lands it ne'er is well With sons of trade who buy and sell: No men who pleasant tales repeat Delight the crowd with stories sweet. In kingless realms we ne'er behold Young maidens decked with gems and gold, Flock to the gardens blithe and gay To spend their evening hours in play. No lover in the flying car Rides with his love to woods afar. In kingless lands no wealthy swain Who keeps the herd and reaps the grain, Lies sleeping, blest with ample store, Securely near his open door. Upon the royal roads we see No tusked elephant roaming free, Of three-score years, whose head and neck
- **Translation**: 

---

### Verse 4 (Ramayana 0.629)
- **Original**: Canto LXVII. The Praise Of Kings. 611 Sweet tinkling bells of silver deck. We hear no more the glad applause When his strong bow each rival draws, No clap of hands, no eager cries That cheer each martial exercise. In kingless realms no merchant bands Who travel forth to distant lands, With precious wares their wagons load, [175] And fear no danger on the road. No sage secure in self-control, Brooding on God with mind and soul, In lonely wanderings finds his home Where'er at eve his feet may roam. In kingless realms no man is sure He holds his life and wealth secure. In kingless lands no warriors smite The foeman's host in glorious fight. In kingless lands the wise no more, Well trained in Scripture's holy lore, In shady groves and gardens meet To argue in their calm retreat. No longer, in religious fear, Do they who pious vows revere, Bring dainty cates and wreaths of flowers As offerings to the heavenly powers. No longer, bright as trees in spring, Shine forth the children of the king Resplendent in the people's eyes With aloe wood and sandal dyes. A brook where water once has been, A grove where grass no more is green, Kine with no herdsman's guiding hand— So wretched is a kingless land. The car its waving banner rears,
- **Translation**: 

---

### Verse 5 (Ramayana 0.630)
- **Original**: 612 The Ramayana Banner of fire the smoke appears: Our king, the banner of our pride, A God with Gods is glorified. In kingless lands no law is known, And none may call his wealth his own, Each preys on each from hour to hour, As fish the weaker fish devour. Then fearless, atheists overleap The bounds of right the godly keep, And when no royal powers restrain, Preëminence and lordship gain. As in the frame of man the eye Keeps watch and ward, a careful spy, The monarch in his wide domains Protects the truth, the right maintains. He is the right, the truth is he, Their hopes in him the well-born see. On him his people's lives depend, Mother is he, and sire, and friend. The world were veiled in blinding night, And none could see or know aright, Ruled there no king in any state The good and ill to separate. We will obey thy word and will As if our king were living still: As keeps his bounds the faithful sea, So we observe thy high decree. O best of Bráhmans, first in place, Our kingless land lies desolate: Some scion of Ikshváku's race Do thou as monarch consecrate.”
- **Translation**: 

---

### Verse 6 (Ramayana 0.631)
- **Original**: Canto LXVIII. The Envoys. 613 Canto LXVIII. The Envoys. Va [ishmha heard their speech and prayer, And thus addressed the concourse there, Friends, Bráhmans, counsellors, and all Assembled in the palace hall: “Ye know that Bharat, free from care, Still lives in Rájagriha339 where The father of his mother reigns: Zatrughna by his side remains. Let active envoys, good at need, Thither on fleetest horses speed, To bring the hero youths away: Why waste the time in dull delay?” Quick came from all the glad reply: “Va [ishmha, let the envoys fly!” He heard their speech, and thus renewed His charge before the multitude: “Nandan, A[ok, Siddhárth, attend, Your ears, Jayanta, Vijay, lend: Be yours, what need requires, to do: I speak these words to all of you. With coursers of the fleetest breed To Rájagriha's city speed. Then rid your bosoms of distress, And Bharat thus from me address: “The household priest and peers by us Send health to thee and greet thee thus: Come to thy father's home with haste: Thine absent time no longer waste.” 339 Rájagriha, or Girivraja was the capital of A[vapati, Bharat's maternal grandfather.
- **Translation**: 

---

### Verse 7 (Ramayana 0.632)
- **Original**: 614 The Ramayana But speak no word of Ráma fled, Tell not the prince his sire is dead, Nor to the royal youth the fate That ruins Raghu's race relate. Go quickly hence, and with you bear Fine silken vestures rich and rare, And gems and many a precious thing As gifts to Bharat and the king.” With ample stores of food supplied, Each to his home the envoys hied, Prepared, with steeds of swiftest race, To Kekaya's land340 their way to trace. They made all due provision there, And every need arranged with care, Then ordered by Va[ishmha, they Went forth with speed upon their way. Then northward of Pralamba, west Of Apartála, on they pressed, Crossing the Máliní that flowed With gentle stream athwart the road. They traversed Gangá's holy waves[176] Where she Hástinapura341 laves, Thence to Panchála342 westward fast Through Kurujángal's land343 Note. 340 The Kekayas or Kaikayas in the Punjab appear amongst the chief nations in the war of the Mahábhárata; their king being a kinsman of KrishGa. 341 Hástinapura was the capital of the kingdom of Kuru, near the modern Delhi. 342 The Panchálas occupied the upper part of the Doab. 343 “Kurujángala and its inhabitants are frequently mentioned in the Mahábhárata, as in theÁdi-parv.3789, 4337,et al.” W ILSON 'S{FNS VishGu PuráGa,Vol. II. p. 176. DR . HALL 'S{FNS
- **Translation**: 

---

### Verse 8 (Ramayana 0.633)
- **Original**: Canto LXVIII. The Envoys. 615 they passed. On, on their course the envoys held By urgency of task impelled. Quick glancing at each lucid flood And sweet lake gay with flower and bud. Beyond, they passed unwearied o'er, Where glad birds fill the flood and shore Of ZaradaG á racing fleet With heavenly water clear and sweet, Thereby a tree celestial grows Which every boon on prayer bestows: To its blest shade they humbly bent, Then to Kulingá's town they went. Then, having passed the Warrior's Wood, In Abhikála next they stood, O'er sacred Ikshumatí344 Edition. The Ikshumatí was a river in Kurukshetra. came, Their ancient kings' ancestral claim. They saw the learned Bráhmans stand, Each drinking from his hollowed hand, And through Báhíka345 journeying still They reached at length Sudáman's hill: There VishGu's footstep turned to see, Vipá[á346 viewed, andZálmalí, And many a lake and river met, Tank, pool, and pond, and rivulet. 344 “The I¾{¼±Ä¹Â of Arrian. SeeAs. Res. Vol. XV. p. 420, 421, also Indische Alterthumskunde, Vol. I. p. 602, first footnote.” W ILSON 'S{FNS VishGu PuráGa, Vol. I. p. 421. DR . HALL 'S{FNS 345 “The Báhíkas are described in the Mahábhárata, KarGa Parvan, with some detail, and comprehend the different nations of the Punjab from the Sutlej to the Indus.” W ILSON 'S{FNS VishGu PuráGa, Vol. I. p. 167. 346 The Beas, Hyphasis, or Bibasis.
- **Translation**: 

---

### Verse 9 (Ramayana 0.634)
- **Original**: 616 The Ramayana And lions saw, and tigers near, And elephants and herds of deer, And still, by prompt obedience led, Along the ample road they sped. Then when their course so swift and long, Had worn their steeds though fleet and strong, To Girivraja's splendid town They came by night, and lighted down. To please their master, and to guard The royal race, the lineal right, The envoys, spent with riding hard, To that fair city came by night.347 347 It would be lost labour to attempt to verify all the towns and streams mentioned in Cantos LXVIII and LXXII. Professor Wilson observes (VishGu PuráGa, p. 139. Dr. Hall's Edition)“States, and tribes, and cities have disap- peared, even from recollection; and some of the natural features of the country, especially the rivers, have undergone a total alteration.… Notwithstanding these impediments, however, we should be able to identify at least mountains and rivers, to a much greater extent than is now practicable, if our maps were not so miserably defective in their nomenclature. None of our surveyors or geographers have been oriental scholars. It may be doubted if any of them have been conversant with the spoken language of the country. They have, consequently, put down names at random, according to their own inaccurate appreciation of sounds carelessly, vulgarly, and corruptly uttered; and their maps of India are crowded with appellations which bear no similitude whatever either to past or present denominations. We need not wonder that we cannot discover Sanskrit names in English maps, when, in the immediate vicinity of Calcutta, Barnagore represents Baráhanagar, Dakshine[war is metamorphosed into Duckinsore, Ulubaría into Willoughbury.… There is scarcely a name in our Indian maps that does not afford proof of extreme indifference to accuracy in nomenclature, and of an incorrectness in estimating sounds, which is, in some degree, perhaps, a national defect.” For further information regarding the road from Ayodhyá to Rájagriha, see
- **Translation**: 

---

### Verse 10 (Ramayana 0.635)
- **Original**: Canto LXIX. Bharat's Dream. 617 Canto LXIX. Bharat's Dream. The night those messengers of state Had past within the city's gate, In dreams the slumbering Bharat saw A sight that chilled his soul with awe. The dream that dire events foretold Left Bharat's heart with horror cold, [177] And with consuming woes distraught, Upon his aged sire he thought. His dear companions, swift to trace The signs of anguish on his face, Drew near, his sorrow to expel, And pleasant tales began to tell. Some woke sweet music's cheering sound, And others danced in lively round. With joke and jest they strove to raise His spirits, quoting ancient plays; But Bharat still, the lofty-souled, Deaf to sweet tales his fellows told, Unmoved by music, dance, and jest, Sat silent, by his woe oppressed. To him, begirt by comrades near, Thus spoke the friend he held most dear: “Why ringed around by friends, art thou So silent and so mournful now?” “Hear thou,” thus Bharat made reply, “What chills my heart and dims mine eye. I dreamt I saw the king my sire Sink headlong in a lake of mire Down from a mountain high in air, His body soiled, and loose his hair. Additional Notes.
- **Translation**: 

---

### Verse 11 (Ramayana 0.636)
- **Original**: 618 The Ramayana Upon the miry lake he seemed To lie and welter, as I dreamed; With hollowed hands full many a draught Of oil he took, and loudly laughed. With head cast down I saw him make A meal on sesamum and cake; The oil from every member dripped, And in its clammy flood he dipped. The ocean's bed was bare and dry, The moon had fallen from the sky, And all the world lay still and dead, With whelming darkness overspread. The earth was rent and opened wide, The leafy trees were scorched, and died; I saw the seated mountains split, And wreaths of rising smoke emit. The stately beast the monarch rode His long tusks rent and splintered showed; And flames that quenched and cold had lain Blazed forth with kindled light again. I looked, and many a handsome dame, Arrayed in brown and sable came And bore about the monarch, dressed, On iron stool, in sable vest. And then the king, of virtuous mind, A blood-red wreath around him twined, Forth on an ass-drawn chariot sped, As southward still he bent his head. Then, crimson-clad, a dame appeared Who at the monarch laughed and jeered; And a she-monster, dire to view, Her hand upon his body threw. Such is the dream I dreamt by night, Which chills me yet with wild affright:
- **Translation**: 

---

### Verse 12 (Ramayana 0.637)
- **Original**: Canto LXX. Bharat's Departure. 619 Either the king or Ráma, I Or LakshmaG now must surely die. For when an ass-drawn chariot seems To bear away a man in dreams, Be sure above his funeral pyre The smoke soon rears its cloudy spire. This makes my spirit low and weak, My tongue is slow and loth to speak: My lips and throat are dry for dread, And all my soul disquieted. My lips, relaxed, can hardly speak, And chilling dread has changed my cheek I blame myself in aimless fears, And still no cause of blame appears. I dwell upon this dream of ill Whose changing scenes I viewed, And on the startling horror still My troubled thoughts will brood. Still to my soul these terrors cling, Reluctant to depart, And the strange vision of the king Still weighs upon my heart.” Canto LXX. Bharat's Departure. While thus he spoke, the envoys borne On horses faint and travel-worn Had gained the city fenced around With a deep moat's protecting bound. An audience of the king they gained, And honours from the prince obtained;
- **Translation**: 

---

### Verse 13 (Ramayana 0.638)
- **Original**: 620 The Ramayana The monarch's feet they humbly pressed, To Bharat next these words addressed: “The household priest and peers by us Send health to thee and greet thee thus: “Come to thy father's house with haste: Thine absent time no longer waste.” Receive these vestures rich and rare, These costly gems and jewels fair, And to thy uncle here present Each precious robe and ornament. These for the king and him suffice— Two hundred millions is their price— These, worth a hundred millions, be Reserved, O large-eyed Prince, for thee.” Loving his friends with heart and soul, The joyful prince received the whole, Due honour to the envoys paid, And thus in turn his answer made: “Of Da[aratha tidings tell: Is the old king my father well? Is Ráma, and is LakshmaG, he Of the high-soul, from sickness free? And she who walks where duty leads, Kau [alyá, known for gracious deeds, Mother of Ráma, loving spouse, Bound to her lord by well kept vows? And Lakshma G's mother too, the dame Sumitrá skilled in duty's claim, Who brave Zatrughna also bare, Second in age,— her health declare.[178] And she, in self-conceit most sage, With selfish heart most prone to rage, My mother, fares she well? has she
- **Translation**: 

---

### Verse 14 (Ramayana 0.639)
- **Original**: Canto LXX. Bharat's Departure. 621 Sent message or command to me?” Thus Bharat spake, the mighty-souled, And they in brief their tidings told: “All they of whom thou askest dwell, O lion lord, secure and well: Thine all the smiles of fortune are: Make ready; let them yoke the car.” Thus by the royal envoys pressed, Bharat again the band addressed: “I go with you: no long delay, A single hour I bid you stay.” Thus Bharat, son of him who swayed Ayodhyás realm, his answer made, And then bespoke, his heart to please, His mother's sire in words like these: “I go to see my father, King, Urged by the envoys' summoning; And when thy soul desires to see Thy grandson, will return to thee.” The king his grandsire kissed his head, And in reply to Bharat said: “Go forth, dear child: how blest is she, The mother of a son like thee! Greet well thy sire, thy mother greet, O thou whose arms the foe defeat; The household priest, and all the rest Amid the Twice-born chief and best; And Ráma and brave LakshmaG, who Shoot the long shaft with aim so true.”
- **Translation**: 

---

### Verse 15 (Ramayana 0.640)
- **Original**: 622 The Ramayana To him the king high honour showed, And store of wealth and gifts bestowed, The choicest elephants to ride, And skins and blankets deftly dyed, A thousand strings of golden beads, And sixteen hundred mettled steeds: And boundless wealth before him piled Gave Kekaya to Kaikeyí's child. And men of counsel, good and tried, On whose firm truth he aye relied, King A[vapati gave with speed Prince Bharat on his way to lead. And noble elephants, strong and young, From sires of Indra[ira sprung, And others tall and fair to view Of great Airávat's lineage true: And well yoked asses fleet of limb The prince his uncle gave to him. And dogs within the palace bred, Of body vast and massive head, With mighty fangs for battle, brave, The tiger's match in strength, he gave. Yet Bharat's bosom hardly glowed To see the wealth the king bestowed; For he would speed that hour away, Such care upon his bosom lay: Those eager envoys urged him thence, And that sad vision's influence. He left his court-yard, crowded then With elephants and steeds and men, And, peerless in immortal fame, To the great royal street he came. He saw, as farther still he went, The inner rooms most excellent,
- **Translation**: 

---

### Verse 16 (Ramayana 0.641)
- **Original**: Canto LXXI. Bharat's Return. 623 And passed the doors, to him unclosed, Where check nor bar his way oppossd. There Bharat stayed to bid adieu To grandsire and to uncle too, Then, withZatrughna by his side, Mounting his car, away he hied. The strong-wheeled cars were yoked, and they More than a hundred, rolled away: Servants, with horses, asses, kine, Followed their lord in endless line. So, guarded by his own right hand, Forth high-souled Bharat hied, Surrounded by a lordly band On whom the king relied. Beside him satZatrughna dear, The scourge of trembling foes: Thus from the light of Indra's sphere A saint made perfect goes. Canto LXXI. Bharat's Return. Then Bharat's face was eastward bent As from the royal town he went. He reached Sudámá's farther side, And glorious, gazed upon the tide; Passed Hládiní, and saw her toss Her westering billows hard to cross. Then old Ikshváku's famous son O'erZatadrú348 his passage won, 348 “The Zatadrú,‘the hundred-channeled’— the Zaradrus of Ptolemy, Hesydrus of Pliny— is the Sutlej.” W ILSON 'S{FNS VishGu PuráGa, Vol. II. p. 130.
- **Translation**: 

---

### Verse 17 (Ramayana 0.642)
- **Original**: 624 The Ramayana Near Ailadhána on the strand, And came to Aparparyat's land. O'erZilá's flood he hurried fast, Akurvatí's fair stream he passed, Crossed o'er Ágneya's rapid rill, And Zalyakartan onward still. Zilávahá's swift stream he eyed, True to his vows and purified, Then crossed the lofty hills, and stood In Chaitraratha's mighty wood. He reached the confluence where meet Sarasvatí349 and Gangá fleet, And through BháruG a forest, spread Northward of Viramatsya, sped. He sought Kálinda's child, who fills[179] The soul with joy, begirt by hills, Reached Yamuná, and passing o'er, Rested his army on the shore: He gave his horses food and rest, Bathed reeking limb and drooping crest. They drank their fill and bathed them there, And water for their journey bare. Thence through a mighty wood he sped All wild and uninhabited, As in fair chariot through the skies, Most fair in shape a Storm-God flies. At An[udhána Gangá, hard To cross, his onward journey barred, So turning quickly thence he came To Prágvam's city dear to fame. There having gained the farther side To Kumikoshmiká he hied: 349 The Sarasvatí or Sursooty is a tributary of the Caggar or Guggur in Sirhind.
- **Translation**: 

---

### Verse 18 (Ramayana 0.643)
- **Original**: Canto LXXI. Bharat's Return. 625 The stream he crossed, and onward then To Dharmavardhan brought his men. Thence, leaving ToraG on the north, To Jambuprastha journeyed forth. Then onward to a pleasant grove By fair Varútha's town he drove, And when a while he there had stayed, Went eastward from the friendly shade. Eastward of Ujjiháná where The Priyak trees are tall and fair, He passed, and rested there each steed Exhausted with the journey's speed. There orders to his men addressed, With quickened pace he onward pressed, A while at Sarvatírtha spent, Then o'er Uttániká he went. O'er many a stream beside he sped With coursers on the mountains bred, And passing Hastiprishmhak, took The road o'er Kumiká's fair brook. Then, at Lohitya's village, he Crossed o'er the swift Kapívatí, Then passed, where Eka[ála stands, The StháGumatí's flood and sands, And Gomatí of fair renown By Vinata's delightful town. When to Kalinga near he drew, A wood of Sal trees charmed the view; That passed, the sun began to rise, And Bharat saw with happy eyes, Ayodhyá's city, built and planned By ancient Manu's royal hand. Seven nights upon the road had passed, And when he saw the town at last
- **Translation**: 

---

### Verse 19 (Ramayana 0.644)
- **Original**: 626 The Ramayana Before him in her beauty spread, Thus Bharat to the driver said: “This glorious city from afar, Wherein pure groves and gardens are, Seems to my eager eyes to-day A lifeless pile of yellow clay. Through all her streets where erst a throng Of men and women streamed along, Uprose the multitudinous roar: To-day I hear that sound no more. No longer do mine eyes behold The leading people, as of old, On elephants, cars, horses, go Abroad and homeward, to and fro. The brilliant gardens, where we heard The wild note of each rapturous bird, Where men and women loved to meet, In pleasant shades, for pastime sweet,— These to my eyes this day appear Joyless, and desolate, and drear: Each tree that graced the garden grieves, And every path is spread with leaves. The merry cry of bird and beast, That spake aloud their joy, has ceased: Still is the long melodious note That charmed us from each warbling throat. Why blows the blessed air no more, The incense-breathing air that bore Its sweet incomparable scent Of sandal and of aloe blent? Why are the drum and tabour mute? Why is the music of the lute That woke responsive to the quill, Loved by the happy, hushed and still?
- **Translation**: 

---

### Verse 20 (Ramayana 0.645)
- **Original**: Canto LXXI. Bharat's Return. 627 My boding spirit gathers hence Dire sins of awful consequence, And omens, crowding on my sight, Weigh down my soul with wild affright. Scarce shall I find my friends who dwell Here in Ayodhyá safe and well: For surely not without a cause This crushing dread my soul o'erawes.” Heart sick, dejected, every sense Confused by terror's influence, On to the town he quickly swept Which King Ikshváku's children kept. He passed through Vaijayanta's gate, With weary steeds, disconsolate, And all who near their station held, His escort, crying Victory, swelled, With heart distracted still he bowed Farewell to all the following crowd, Turned to the driver and began To question thus the weary man: “Why was I brought, O free from blame, So fast, unknown for what I came? Yet fear of ill my heart appals, And all my wonted courage falls. For I have heard in days gone by The changes seen when monarchs die; And all those signs, O charioteer, I see to-day surround me here: Each kinsman's house looks dark and grim, No hand delights to keep it trim: The beauty vanished, and the pride, The doors, unkept, stand open wide. No morning rites are offered there,
- **Translation**: 

---

