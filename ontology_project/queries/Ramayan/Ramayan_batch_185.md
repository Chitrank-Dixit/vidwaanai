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

### Verse 1 (Ramayana 0.1726)
- **Original**: 1708 The Ramayana O'er hill and plain and watery waste His rapid way again he traced. And mid the wondering Vánars laid His burthen through the air conveyed, The wondrous herbs' delightful scent To all the host new vigour lent. Free from all darts and wounds and pain The sons of Raghu lived again, And dead and dying Vánars healed Rose vigorous from the battle field. Canto LXXV. The Night Attack. Sugríva spake in words like these: “Now, Vánar lords, the occasion seize. For now, of sons and brothers reft, To RávaG little hope is left: And if our host his gates assail His weak defence will surely fail.”
- **Translation**: 

---

### Verse 2 (Ramayana 0.1727)
- **Original**: Canto LXXV. The Night Attack. 1709 At dead of night the Vánar bands Rushed on with torches in their hands. Scared by the coming of the host Each giant warder left his post. Where'er the Vánar legions came Their way was marked with hostile flame That spread in fury to devour Palace and temple, gate and tower. Down came the walls and porches, down Came stately piles that graced the town. In many a house the fire was red, On sandal wood and aloe fed. And scorching flames in billows rolled O'er diamonds and pearls and gold. On cloth of wool, on silk brocade, On linen robes their fury preyed. Wheels, poles and yokes were burned, and all The coursers' harness in the stall; And elephants' and chariots' gear, The sword, the buckler, and the spear. Scared by the crash of falling beams, Mid lamentations, groans and screams, Forth rushed the giants through the flames And with them dragged bewildered dames, Each, with o'erwhelming terror wild, Still clasping to her breast a child. The swift fire from a cloud of smoke Through many a gilded lattice broke, And, melting pearl and coral, rose O'er balconies and porticoes. The startled crane and peacock screamed As with strange light the courtyard gleamed, And fierce unusual glare was thrown On shrinking wood and heated stone.
- **Translation**: 

---

### Verse 3 (Ramayana 0.1728)
- **Original**: 1710 The Ramayana From burning stall and stable freed Rushed frantic elephant and steed, And goaded by the driving blaze Fled wildly through the crowded ways. As earth with fervent heat will glow When comes her final overthrow; From gate to gate, from court to spire Proud Lanká was one blaze of fire, And every headland, rock and bay Shone bright a hundred leagues away. Forth, blinded by the heat and flame Ran countless giants huge of frame; And, mustering for fierce attack, The Vánars charged to drive them back, While shout and scream and roar and cry Reëchoed through the earth and sky. There Ráma stood with strength renewed, And ever, as the foe he viewed, Shaking the distant regions rang His mighty bow's tremendous clang. Then through the gates Nikumbha hied, And Kumbha by his brother's side, Sent forth— the bravest and the best— To battle by the king's behest. There fought the chiefs in open field, And Angad fell and Dwivid reeled. Sugríva saw: by rage impelled He crushed the bow which Kumbha held. About his foe Sugríva wound His arms, and, heaving from the ground The giant hurled him o'er the bank; And deep beneath the sea he sank. Like mandar hill with furious swell Up leapt the waters where he fell.
- **Translation**: 

---

### Verse 4 (Ramayana 0.1729)
- **Original**: Canto LXXV. The Night Attack. 1711 Again he rose: he sprang to land And raised on high his threatening hand: Full on Sugríva's chest it came And shook the Vánar's massy frame, But on the wounded bone he broke His wrist— so furious was the stroke. With force that naught could stay or check, Sugríva smote him neath the neck. The fierce blow crashed through flesh and bone And Kumbha lay in death o'erthrown. Nikumbha saw his brother die, And red with fury flashed his eye. He dashed with mighty sway and swing [485] His axe against the Vánar king; But shattered on that living rock It split in fragments at the shock. Sugríva, rising to the blow, Raised his huge hand and smote his foe. And in the dust the giant lay Gasping in blood his soul away. [I have briefly despatched Kumbha and Nikumbha, each of whom has in the text a long Canto to himself. When they fall RávaG sends forth Makaráksha or Crocodile-Eye, the son of Khara who was slain by Ráma in the forest before the abduction of Sítá. The account of his sallying forth, of his battle with Ráma and of his death by the fiery dart of that hero occupies two Cantos which I entirely pass over. Indrajít again comes forth and, ren- dered invisible by his magic art slays countless Vánars with his unerring arrows. He retires to the city and returns bearing in his chariot an effigy of Sítá, the work of magic, weeping and wailing by his side. He grasps the lovely image by the hair and cuts it down with his scimitar in the sight of the enraged Hanúmán and all the Vánar host. At last after much fighting of the usual kind Indrajít's chariot is broken in pieces, his charioteer is slain,
- **Translation**: 

---

### Verse 5 (Ramayana 0.1730)
- **Original**: 1712 The Ramayana and he himself falls by LakshmaG's hand, to the inexpressible delight of the high-souled saints, the nymphs of heaven and other celestial beings.] Canto XCIII. Rávan's Lament. They sought the king, a mournful train, And cried,“My lord, thy son is slain. By LakshmaG's hand, before these eyes, The warrior fell no more to rise. No time is this for vain regret: Thy hero son a hero met; And he whose might in battle pressed Lord Indra and the Gods confessed, Whose power was stranger to defeat, Has gained in heaven a blissful seat.” The monarch heard the mournful tale: His heart was faint, his cheek was pale; His fleeting sense at length regained, In trembling tones he thus complained: “Ah me, my son, my pride: the boast And glory of the giant host. Could LakshmaG's puny might defeat The foe whom Indra feared to meet? Could not thy deadly arrows split Proud Mandar's peaks, O Indrajít, And the Destroyer's self destroy? And wast thou conquered by a boy? I will not weep: thy noble deed Has blessed thee with immortal meed
- **Translation**: 

---

### Verse 6 (Ramayana 0.1731)
- **Original**: Canto XCIII. Rávan's Lament. 1713 Gained by each hero in the skies Who fighting for his sovereign dies. Now, fearless of all meaner foes, The guardian Gods993 will taste repose: But earth to me, with hill and plain, Is desolate, for thou art slain. Ah, whither hast thou fled, and left Thy mother, Lanká, me bereft; Left pride and state and wives behind, And lordship over all thy kind? I fondly hoped thy hand should pay Due honours on my dying day: And couldst thou, O beloved, flee And leave thy funeral rites to me? Life has no comfort left me, none, O Indrajít my son, my son.” Thus wailed he broken by his woes: But swift the thought of vengeance rose. In awful wrath his teeth he gnashed, And from his eyes red lightning flashed. Hot from his mouth came fire and smoke, As thus the king in fury spoke: 993 The Lokapálas are sometimes regarded as deities appointed by Brahmá at the creation of the word to act as guardians of different orders of beings, but more commonly they are identified with the deities presiding over the four cardinal and four intermediate points of the compass, which, according to Manu V. 96, are 1, Indra, guardian of the East; 2, Agni, of the South-east; 3, Yáma, of the South; 4, Súrya, of the South-west; 5, VaruGa, of the West; 6, Pavana or Váyu, of the North-west; 7, Kuvera, of the North; 8, Soma or Chandra, of the North-east.
- **Translation**: 

---

### Verse 7 (Ramayana 0.1732)
- **Original**: 1714 The Ramayana “Through many a thousand years of yore The penance and the pain I bore, And by fierce torment well sustained The highest grace of Brahmá gained, His plighted word my life assured, From Gods of heaven and fiends secured. He armed my limbs with burnished mail Whose lustre turns the sunbeams pale, In battle proof gainst heavenly bands With thunder in their threatening hands. Armed in this mail myself will go With Brahmá's gift my deadly bow, And, cleaving through the foes my way, The slayers of my son will slay.” Then, by his grief to frenzy wrought, The captive in the grove he sought. Swift through the shady path he sped: Earth trembled at his furious tread. Fierce were his eyes: his monstrous hand Held drawn for death his glittering brand.[486] There weeping stood the Maithil dame: She shuddered as the giant came. Near drew the rover of the night And raised his sword in act to smite; But, by his nobler heart impelled, One Rákshas lord his arm withheld: “Wilt thou, great Monarch,” thus he cried, “Wilt thou, to heavenly Gods allied, Blot for all time thy glorious fame, The slayer of a gentle dame? What! shall a woman's blood be spilt To stain thee with eternal guilt, Thee deep in all the Veda's lore?
- **Translation**: 

---

### Verse 8 (Ramayana 0.1733)
- **Original**: Canto XCVI. Rávan's Sally. 1715 Far be the thought for evermore. Ah look, and let her lovely face This fury from thy bosom chase.” He ceased: the prudent counsel pleased The monarch, and his wrath appeased; Then to his council hall in haste The giant lord his steps retraced. [I omit two Cantos in the first of which Ráma with an enchanted Gandharva weapon deals destruction among the Rákshases sent out by RávaG, and in the second the Rákshas dames lament the slain and mourn over the madness of RávaG.] Canto XCVI. Rávan's Sally. The groans and cries of dames who wailed The ears of Lanká's lord assailed, For from each house and home was sent The voice of weeping and lament. In troubled thought his head he bowed, Then fiercely loosing on the crowd Of nobles near his throne he broke The silence, and in fury spoke: “This day my deadly shafts shall fly, And Raghu's sons shall surely die. This day shall countless Vánars bleed And dogs and kites and vultures feed. Go, bid them swift my car prepare, Bring the great bow I long to bear: And let my host with sword and shield And spear be ready for the field.”
- **Translation**: 

---

### Verse 9 (Ramayana 0.1734)
- **Original**: 1716 The Ramayana From street to street the captains passed And Rákshas warriors gathered fast. With spear and sword to pierce and strike, And axe and club and mace and pike. [I omit several weapons for which I cannot find distinctive names, and among them theSataghníor Centicide, supposed by some to be a kind of fire-arms or rocket, but described by a commentator on the Mahábhárata as a stone or cylindrical piece of wood studded with iron spikes.] Then RávaG's warrior chariot994 wrought With gold and rich inlay was brought. Mid tinkling bells and weapons' clang The monarch on the chariot sprang, Which, decked with gems of every hue, Eight steeds of noble lineage drew. Mid roars of drum and shell rang out From countless throats a joyful shout. As, girt with hosts in warlike pride, Through Lanká's streets the tyrant hied. Still, louder than the roar of drums, Went up the cry“He comes, he comes, Our ever conquering lord who trod Beneath his feet both fiend and God.” On to the gate the warriors swept Where Raghu's sons their station kept. When Ráva G's car the portal passed The sun in heaven was overcast. Earth rocked and reeled from side to side And birds with boding voices cried. 994 The chariots of RávaG's present army are said to have been one hundred and fifty million in number with three hundred million elephants, and twelve hundred million horses and asses. The footmen are merely said to have been “unnumbered.”
- **Translation**: 

---

### Verse 10 (Ramayana 0.1735)
- **Original**: Canto C. Rávan In The Field. 1717 Against the standard of the king A vulture flapped his horrid wing. Big gouts of blood before him dropped, His trembling steeds in terror stopped. The hue of death was on his cheek, And scarce his flattering tongue could speak, When, terrible with flash and flame, Through murky air a meteor came. Still by the hand of Death impelled His onward way the giant held. The Vánars in the field afar Heard the loud thunder of his car. And turned with warriors' fierce delight To meet the giant in the fight. He came: his clanging bow he drew And myriads of the Vánars slew. Some through the side and heart he cleft, Some headless on the plain were left. Some struggling groaned with mangled thighs, Or broken arms or blinded eyes. [I omit Cantos XCVII, XCVIII, and XCIX, which describe in the usual way three single combats between Sugríva and Angad on the Vánar side and Virúpáksha, Mahodar, and Mahápár[va on the side of the giants. The weapons of the Vánars are trees and rocks; the giants fight with swords, axes, and bows and arrows. The details are generally the same as those of preceding duels. The giants fall, one in each Canto.] [487] Canto C. Rávan In The Field.
- **Translation**: 

---

### Verse 11 (Ramayana 0.1736)
- **Original**: 1718 The Ramayana The plain with bleeding limbs was spread, And heaps of dying and of dead. His mighty bow still Ráma strained, And shafts upon the giants rained. Still Angad and Sugríva, wrought To fury, for the Vánars fought. Crushed with huge rocks through chest and side Mahodar, Mahápár[va died, And Virúpáksha stained with gore Dropped on the plain to rise no more. When Ráva G saw the three o'erthrown He cried aloud in furious tone: “Urge, urge the car, my charioteer, The haughty Vánars' death is near. This very day shall end our griefs For leaguered town and slaughtered chiefs. Ráma the tree whose lovely fruit Is Sítá, shall this arm uproot,— Whose branches with protecting shade Are Vánar lords who lend him aid.” Thus cried the king: the welkin rang As forth the eager coursers sprang, And earth beneath the chariot shook With flowery grove and hill and brook. Fast rained his shafts: where'er he sped The conquered Vánars fell or fled, On rolled the car in swift career Till Raghu's noble sons were near. Then Ráma looked upon the foe And strained and tried his sounding bow, Till earth and all the region rang Re-echoing to the awful clang. His bow the younger chieftain bent,
- **Translation**: 

---

### Verse 12 (Ramayana 0.1737)
- **Original**: Canto C. Rávan In The Field. 1719 And shaft on shaft at RávaG sent. He shot: but RávaG little recked; Each arrow with his own he checked, And headless, baffled of its aim, To earth the harmless missile came; And Lakshma G stayed his arm o'erpowered By the thick darts the giant showered. Fierce waxed the fight and fiercer yet, For RávaG now and Ráma met, And each on other poured amain The tempest of his arrowy rain. While all the sky above was dark With missiles speeding to their mark Like clouds, with flashing lightning twined About them, hurried by the wind. Not fiercer was the wondrous fight When Vritra fell by Indra's might. All arts of war each foeman knew, And trained alike, his bowstring drew. Red-eyed with fury Lanká's king Pressed his huge fingers on the string, And fixed in Ráma's brows a flight Of arrows winged with matchless flight. Still Raghu's son endured, and bore That crown of shafts though wounded sore. O'er a dire dart a spell he spoke With mystic power to aid the stroke. In vain upon the foe it smote Rebounding from the steelproof coat. The giant armed his bow anew, And wondrous weapons hissed and flew, Terrific, deadly, swift of flight, Beaked like the vulture and the kite, Or bearing heads of fearful make,
- **Translation**: 

---

### Verse 13 (Ramayana 0.1738)
- **Original**: 1720 The Ramayana Of lion, tiger, wolf and snake.995 Then Ráma, troubled by the storm Of flying darts in every form Shot by an arm that naught could tire, Launched at the foe his dart of fire, Which, sacred to the Lord of Flame, Burnt and consumed where'er it came. And many a blazing shaft beside The hero to his string applied. With fiery course of dazzling hue Swift to the mark each missile flew, Some flashing like a shooting star, Some as the tongues of lightning are; One like a brilliant plant, one In splendour like the morning sun. Where'er the shafts of Ráma burned The giant's darts were foiled and turned. Far into space his weapons fled, But as they flew struck thousands dead. Canto CI. Lakshman's Fall. When Ráva G saw his darts repelled, With double rage his bosom swelled. He summoned, wroth but undismayed, A mightier charm to lend its aid. 995 It is not very easy to see the advantage of having arrows headed in the way mentioned. Fanciful names for war-engines and weapons derived from their resemblance to various animals are not confined to India. The“War-wolf” was used by Edward I. at the siege of Brechin, the“Cat-house” and the“Sow ” were used by Edward III. at the siege of Dunbar.
- **Translation**: 

---

### Verse 14 (Ramayana 0.1739)
- **Original**: Canto CI. Lakshman's Fall. 1721 And, fierce as fire before the blast, A storm of missiles thick and fast, Spear, pike and javelin, mace and brand, Came hurtling from the giant's hand. But, mightier still, the arms employed By Raghu's son their force destroyed, And every dart fell dulled and spent By powers the bards of heaven had lent. With his huge mace VibhishaG slew The steeds that RávaG's chariot drew. [488] Then RávaG hurled in deadly ire A ponderous spear that flashed like fire: But Ráma's arrows checked its way, And harmless on the earth it lay, The giant seized a mightier spear, Which Death himself would shun with fear. VibhishaG with the stroke had died, But LakshmaG's hand his bowstring plied, And flying arrows thick as hail Smote fiercely on the giant's mail. Then RávaG turned his aim aside, On Lakshma G looked and fiercely cried: “Thou, thou again my wrath hast braved, And from his death VibhishaG saved. Now in his stead this spear receive Whose deadly point thy heart shall cleave.” He ceased: he hurled the mortal dart By Maya forged with magic art. The spear, with all his fury flung, Swift, flickering like a serpent's tongue, Adorned with many a tinkling bell, Smote LakshmaG, and the hero fell. When Ráma saw, he heaved a sigh,
- **Translation**: 

---

### Verse 15 (Ramayana 0.1740)
- **Original**: 1722 The Ramayana A tear one moment dimmed his eye. But tender grief was soon repressed And thoughts of vengeance filled his breast. The air around him flashed and gleamed As from his bow the arrows streamed; And Lanká's lord, the foeman's dread, O'erwhelmed with terror turned and fled. Canto CII. Lakshman Healed. But Ráma, pride of Raghu's race, Gazed tenderly on LakshmaG's face, And, as the sight his spirit broke, Turned to SusheG and sadly spoke: “Where is my power and valour? how Shall I have heart for battle now, When dead before my weeping eyes My brother, noblest LakshmaG, lies? My tears in blinding torrents flow, My hand unnerved has dropped my bow. The pangs of woe have blanched my cheek, My heart is sick, my strength is weak. Ah me, my brother! Ah, that I By LakshmaG's side might sink and die: Life, war and conquest, all are vain If LakshmaG lies in battle slain. Why will those eyes my glances shun? Hast thou no word of answer, none? Ah, is thy noble spirit flown And gone to other worlds alone? Couldst thou not let thy brother seek
- **Translation**: 

---

### Verse 16 (Ramayana 0.1741)
- **Original**: Canto CII. Lakshman Healed. 1723 Those worlds with thee? O speak, O speak! Rise up once more, my brother, rise, Look on me with thy loving eyes. Were not thy steps beside me still In gloomy wood, on breezy hill? Did not thy gentle care assuage Thy brother's grief and fitful rage? Didst thou not all his troubles share, His guide and comfort in despair?” As Ráma, vanquished, wept and sighed The Vánar chieftain thus replied: “Great Prince, unmanly thoughts dismiss, Nor yield thy soul to grief like this. In vain those burning tears are shed: Our glory LakshmaG is not dead. Death on his brow no mark has set, Where beauty's lustre lingers yet. Clear is the skin, and tender hues Of lotus flowers his palms suffuse. O Ráma, cheer thy trembling heart; Not thus do life and body part. Now, Hanumán, to thee I speak: Hie hence to tall Mahodaya's996 peak Where herbs of sovereign virtue grow Which life and health and strength bestow Bring thou the leaves to balm his pain, And Lakshma G shall be well again.” 996 Apparently a peak of the Himalaya chain.
- **Translation**: 

---

### Verse 17 (Ramayana 0.1742)
- **Original**: 1724 The Ramayana He ceased: the Wind-God's son obeyed Swift through the clouds his way he made. He reached the hill, nor stayed to find The wondrous herbs of healing kind, From its broad base the mount he tore With all the shrubs and trees it bore, Sped through the clouds again and showed To wise SusheG his woody load.997 SusheG in wonder viewed the hill, And culled the sovereign salve of ill. Soon as the healing herb he found, The fragrant leaves he crushed and ground. Then over LakshmaG's face he bent, Who, healed and strengthened by the scent Of that blest herb divinely sweet, Rose fresh and lusty on his feet. Canto CIII. Indra's Car. Then Raghu's son forgot his woe: Again he grasped his fallen bow And hurled at Lanká's lord amain The tempest of his arrowy rain.[489] 997 This exploit of Hanumán is related with inordinate prolixity in the Bengal recension (Gortesio's text). Among other adventures he narrowly escapes being shot by Bharat as he passes over Nandigrama near Ayodhyá. Hanumán stays Bharat in time, and gives him an account of what has befallen Ráma and Sítá in the forest and in Lanká.
- **Translation**: 

---

### Verse 18 (Ramayana 0.1743)
- **Original**: Canto CIII. Indra's Car. 1725 Drawn by the steeds his lords had brought, Again the giant turned and fought. And drove his glittering chariot nigh As springs the Day-God through the sky. Then, as his sounding bow he bent, Like thunderbolts his shafts were sent, As when dark clouds in rain time shed Fierce torrents on a mountain's head. High on his car the giant rode, On foot the son of Raghu strode. The Gods from their celestial height Indignant saw the unequal fight. Then he whom heavenly hosts revere, Lord Indra, called his charioteer: “Haste, Mátali,” he cried,“descend; To Raghu's son my chariot lend. With cheering words the chief address; And all the Gods thy deed will bless.” He bowed; he brought the glorious car Whose tinkling bells were heard afar; Fair as the sun of morning, bright With gold and pearl and lazulite. He yoked the steeds of tawny hue That swifter than the tempest flew. Then down the slope of heaven he hied And stayed the car by Ráma's side. “Ascend, O Chief,” he humbly cried, “The chariot which the Gods provide. The mighty bow of Indra see, Sent by the Gods who favour thee; Behold this coat of glittering mail, And spear and shafts which never fail.”
- **Translation**: 

---

### Verse 19 (Ramayana 0.1744)
- **Original**: 1726 The Ramayana Cheered by the grace the Immortals showed The chieftain on the chariot rode. Then as the car-borne warriors met The awful fight raged fiercer yet. Each shaft that RávaG shot became A serpent red with kindled flame, And round the limbs of Ráma hung With fiery jaws and quivering tongue. But every serpent fled dismayed When Raghu's valiant son displayed The weapon of the Feathered King,998 And loosed his arrows from the string. But RávaG armed his bow anew, And showers of shafts at Ráma flew, While the fierce king in swift career Smote with a dart the charioteer. An arrow shot by RávaG's hand Laid the proud banner on the sand, And Indra's steeds of heavenly strain Fell by the iron tempest slain. On Gods and spirits of the air Fell terror, trembling, and despair. The sea's white billows mounted high With froth and foam to drench the sky. The sun by lurid clouds was veiled, The friendly lights of heaven were paled; And, fiercely gleaming, fiery Mars Opposed the beams of gentler stars. 998 As Garu the king of birds is the mortal enemy of serpents the weapon sacred to him is of course best calculated to destroy the serpent arrows of RávaG.
- **Translation**: 

---

### Verse 20 (Ramayana 0.1745)
- **Original**: Canto CVI. Glory To The Sun. 1727 Then Ráma's eyes with fury blazed As Indra's heavenly spear he raised. Loud rang the bells: the glistering head Bright flashes through the region shed. Down came the spear in swift descent: The giant's lance was crushed and bent. Then RávaG's horses brave and fleet Fell dead beneath his arrowy sleet. Fierce on his foeman Ráma pressed, And gored with shafts his mighty breast. And spouting streams of crimson dyed The weary giant's limbs and side. [I omit Cantos CIV and CV in which the fight is renewed and RávaG severely reprimands his charioteer for timidity and want of confidence in his master's prowess, and orders him to charge straight at Ráma on the next occasion.] Canto CVI. Glory To The Sun. There faint and bleeding fast, apart Stood RávaG raging in his heart. Then, moved with ruth for Ráma's sake, Agastya999 came and gently spake: “Bend, Ráma, bend thy heart and ear The everlasting truth to hear Which all thy hopes through life will bless And crown thine arms with full success. The rising sun with golden rays, 999 The celebrated saint who has on former occasions assisted Ráma with his gifts and counsel.
- **Translation**: 

---

