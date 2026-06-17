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

### Verse 1 (Ramayana 0.1246)
- **Original**: 1228 The Ramayana From hell the white A[vatarí.595 That when my spirit wings its flight Sugríva reign, is just and right. But most unjust, O King, that I, Slain by thy treacherous hand, should lie. Be still, my heart: this earthly state Is darkly ruled by sovereign Fate. The realm is lost and won: defy Thy questioners with apt reply.”596 Canto XVIII. Ráma's Reply. He ceased: and Ráma's heart was stirred At every keen reproach he heard. There Báli lay, a dim dark sun, His course of light and glory run: Or like the bed of Ocean dried Of his broad floods from side to side, Or helpless, as the dying fire, Hushed his last words of righteous ire. Then Ráma, with his spirit moved, The Vánar king in turn reproved: 595 “A [vatara is the name of a chief of the Nágas or serpents which inhabit the regions under the earth; it is also the name of a Gandharva. A[vatarí ought to be the wife of one of the two, but I am not sure that this conjecture is right. The commentator does not say who this A[vatarí is, or what tradition or myth is alluded to. Vimalabodha reads A[vatarí in the nominative case, and explains, A [vatarí is the sun, and as the sun with his rays brings back the moon which has been sunk in the ocean and the infernal regions, so will I bring back Sítá.” G ORRESIO {FNS . 596 That is,“Consider what answer you can give to your accusers when they charge you with injustice in killing me.”
- **Translation**: 

---

### Verse 2 (Ramayana 0.1247)
- **Original**: Canto XVIII. Ráma's Reply. 1229 “Why dost thou, Báli, thus revile, And castest not a glance the while On claims of duty, love, and gain, And customs o'er the world that reign? Why dost thou blame me, rash and blind, Fickle as all thy Vánar kind, Slighting each rule of ancient days Which all the good and prudent praise? This land, each hill and woody chase, Belongs to old Ikshváku's race: With bird and beast and man, the whole Is ours to cherish and control. Now Bharat, prompt at duty's call, Wise, just, and true, is lord of all. Each claim of law, love, gain he knows, And wrath and favour duly shows. A king from truth who never bends, And grace with vigour wisely blends; With valour worthy of his race, He knows the claims of time and place. Now we and other kings of might, By his ensample taught aright, The lands of every region tread That justice may increase and spread. While royal Bharat, wise and just, Rules the broad earth, his glorious trust, Who shall attempt, while he is lord, A deed by Justice held abhorred? We now, as Bharat has decreed, Let justice guide our every deed, And toil each sinner to repress Who scorns the way of righteousness. Thou from that path hast turned aside, And virtue's holy law defied,
- **Translation**: 

---

### Verse 3 (Ramayana 0.1248)
- **Original**: 1230 The Ramayana Left the fair path which kings should tread, And followed pleasure's voice instead. The man who cleaves to duty's law Regards these three with filial awe— The sire, the elder brother, third Him from whose lips his lore he heard. Thus too, for duty's sake, the wise Regard with fond paternal eyes The well-loved younger brother, one Their lore has ripened, and a son. Fine are the laws which guide the good, Abstruse, and hardly understood; Only the soul, enthroned within The breast of each, knows right from sin. But thou art wild and weak of soul, And spurnest, like thy race, control; The true and right thou canst not find, The blind consulting with the blind. Incline thine ear and I will teach The cause that prompts my present speech. This tempest of thy soul assuage, Nor blame me in thine idle rage. On this great sin thy thoughts bestow, The sin for which I lay thee low. Thou, Báli, in thy brother's life Hast robbed him of his wedded wife, And keepest, scorning ancient right, His Rumá for thine own delight. Thy son's own wife should scarcely be More sacred in thine eyes than she. All duty thou hast scorned, and hence Comes punishment for dire offence. For those who blindly do amiss There is, I ween, no way but this:
- **Translation**: 

---

### Verse 4 (Ramayana 0.1249)
- **Original**: Canto XVIII. Ráma's Reply. 1231 To check the rash who dare to stray From customs which the good obey, I may not, sprung of Kshatriya line, [347] Forgive this heinous sin of thine: The laws for those who sin like thee The penalty of death decree. Now Bharat rules with sovereign sway, And we his royal word obey. There was no hope of pardon, none, For the vile deed that thou hast done, That wisest monarch dooms to die The wretch whose crimes the law defy; And we, chastising those who err, His righteous doom administer. My soul accounts Sugríva dear E'en as my brother LakshmaG here. He brings me blessing, and I swore His wife and kingdom to restore: A bond in solemn honour bound When Vánar chieftains stood around. And can a king like me forsake His friend, and plighted promise break? Reflect, O Vánar, on the cause, The sanction of eternal laws, And, justly smitten down, confess Thou diest for thy wickedness. By honour was I bound to lend Assistance to a faithful friend; And thou hast met a righteous fate Thy former sins to expiate. And thus wilt thou some merit win And make atonement for thy sin. For hear me, Vánar King, rehearse
- **Translation**: 

---

### Verse 5 (Ramayana 0.1250)
- **Original**: 1232 The Ramayana What Manu 597 spake in ancient verse,— This holy law, which all accept Who honour duty, have I kept: “Pure grow the sinners kings chastise, And, like the virtuous, gain the skies; By pain or full atonement freed, They reap the fruit of righteous deed, While kings who punish not incur The penalties of those who err.” Mándhátá598 once, a noble king, Light of the line from which I spring, Punished with death a devotee When he had stooped to sin like thee; And many a king in ancient time Has punished frantic sinners' crime, And, when their impious blood was spilt, Has washed away the stain of guilt. Cease, Báli, cease: no more complain: Reproaches and laments are vain, For thou art justly punished: we Obey our king and are not free. Once more, O Báli, lend thine ear Another weightiest plea to hear. For this, when heard and pondered well, Will all complaint and rage dispel. My soul will ne'er this deed repent, Nor was my shaft in anger sent. We take the silvan tribes beset With snare and trap and gin and net, 597 Manu, Book VIII. 318.“But men who have committed offences and have received from kings the punishment due to them, go pure to heaven and become as clear as those who have done well.” 598 Mándhátá was one of the earlier descendants of Ikshváku. His name is mentioned in Ráma's genealogy, p. 81.
- **Translation**: 

---

### Verse 6 (Ramayana 0.1251)
- **Original**: Canto XVIII. Ráma's Reply. 1233 And many a heedless deer we smite From thickest shade, concealed from sight. Wild for the slaughter of the game, At stately stags our shafts we aim. We strike them bounding scared away, We strike them as they stand at bay, When careless in the shade they lie, Or scan the plain with watchful eye. They turn away their heads; we aim, And none the eager hunter blame. Each royal saint, well trained in law Of duty, loves his bow to draw And strike the quarry, e'en as thou Hast fallen by mine arrow now, Fighting with him or unaware,— A Vánar thou.— I little care.599 But yet, O best of Vánars, know That kings who rule the earth bestow Fruit of pure life and virtuous deed, And lofty duty's hard-won meed. Harm not thy lord the king: abstain From act and word that cause him pain; For kings are children of the skies Who walk this earth in men's disguise. But thou, in duty's claims untaught, Thy breast with blinding passion fraught, Assailest me who still have clung To duty, with thy bitter tongue.” 599 I cannot understand how Válmíki could put such an excuse as this into Ráma's mouth. Ráma with all solemn ceremony, has made a league of alliance with Báli's younger brother whom he regards as a dear friend and almost as an equal, and now he winds up his reasons for killing Báli by coolly saying: “Besides you are only a monkey, you know, after all, and as such I have every right to kill you how, when, and where I like.”
- **Translation**: 

---

### Verse 7 (Ramayana 0.1252)
- **Original**: 1234 The Ramayana He ceased: and Báli sore distressed The sovereign claims of law confessed, And freed, o'erwhelmed with woe and shame, The lord of Raghu's race from blame. Then, reverent palm to palm applied, To Ráma thus the Vánar cried: “True, best of men, is every word That from thy lips these ears have heard, It ill beseems a wretch like me To bandy empty words with thee. Forgive the angry taunts that broke From my wild bosom as I spoke. And lay not to my charge, O King,[348] My mad reproaches' idle sting. Thou, in the truth by trial trained, Best knowledge of the right hast gained: And layest, just and pure within, The meetest penalty on sin. Through every bond of law I burst, The boldest sinner and the worst. O let thy right-instructing speech Console my heart and wisely teach.” Like some sad elephant who stands Fast sinking in the treacherous sands, Thus Báli raised despairing eyes; Then spake again with sobs and sighs: “Not for myself, O King, I grieve, For Tárá or the friends I leave, As for sweet Angad, my dear son, My noble, only little one. For, nursed in luxury and bliss, His father he will mourn and miss,
- **Translation**: 

---

### Verse 8 (Ramayana 0.1253)
- **Original**: Canto XVIII. Ráma's Reply. 1235 And like a stream whose fount is dry Will waste away and sink and die,— My own dear child, my only boy, His mother Tárá's hope and joy. Spare him, O son of Raghu, spare The child entrusted to thy care. My Angad and Sugríva treat E'en as thy heart considers meet, For thou, O chief of men, art strong To guard the right and punish wrong. O, if thou wilt thine ear incline To hear these dying words of mine, He and Sugríva will to thee As Bharat and as LakshmaG be. Let not my Tárá, left forlorn, Weep for Sugríva's wrathful scorn; Nor let him, for her lord's offence, Condemn her faithful innocence. And well and wisely may he reign If thy dear grace his power sustain: If, following thee his friend and guide, He turn not from thy hest aside: Thus may he reign with glory, nay Thus to the skies will win his way. Though stayed by Tárá's fond recall, By thy dear hand I longed to fall. Against my brother rushed and fought, And gained the death I long have sought.” Then Ráma thus the prince consoled From whose clear eyes the mists were rolled: “Grieve not for those thou leavest thus, Nor tremble for thyself or us, For we will deal with thine and thee
- **Translation**: 

---

### Verse 9 (Ramayana 0.1254)
- **Original**: 1236 The Ramayana As duty and the laws decree. He who exacts and he who pays, Is justly slain or justly slays, Shall in the life to come have bliss; For each has done his task in this. Thou, wandering from the right, art made Pure by the forfeit thou hast paid. Thy weight of sins is cast aside, And duty's claim is satisfied. Then grieve no more, O Prince, but clear Thy bosom from all doubt and fear, For fate, inexorably stern, Thou hast no power to move or turn. Thy princely Angad still will share My tender love, Sugríva's care; And to thy offspring shall be shown Affection that shall match thine own.” Canto XIX. Tárá's Grief. No answer gave the Vánar king To Ráma's prudent counselling. Battered and bruised by tree and stone, By Ráma's arrow overthrown, Fainting upon the ground he lay, Gasping his troubled life away.
- **Translation**: 

---

### Verse 10 (Ramayana 0.1255)
- **Original**: Canto XIX. Tárá's Grief. 1237 But Tárá in the Vánar's hall Heard tidings of her husband's fall; Heard that a shaft from Ráma's bow Had laid the royal Báli low. Her darling Angad by her side, Distracted from her home she hied. Then nigh the place of battle drew The Vánars, Angad's retinue. They saw the bow-armed Ráma: dread Fell on them, and they turned and fled. Like helpless deer, their leaders slain, So wildly fled the startled train. But Tárá saw, and nearer pressed, And thus the flying band addressed: “O Vánars, ye who ever stand About our king, a trusty band, Where is the lion master? why Forsake ye thus your lord and fly? Say, lies he dead upon the plain, A brother by a brother slain, Or pierced by shafts from Ráma's bow That rain from far upon the foe?” Thus Tárá questioned, and was still: Then, wearers of each shape at will, The Vánars thus with one accord Answered the Lady of their lord: “Turn, Tárá turn, and half undone Save Angad thy beloved son. There Ráma stands in death's disguise, And conquered Báli faints and dies. He by whose strong arm, thick and fast, Uprooted trees and rocks were cast, Lies smitten by a shaft that came
- **Translation**: 

---

### Verse 11 (Ramayana 0.1256)
- **Original**: 1238 The Ramayana Resistless as the lightning flame. When he, whose splendour once could vie With Indra's, regent of the sky, Fell by that deadly arrow, all The Vánars fled who marked his fall. Let all our chiefs their succours bring, And Angad be anointed king;[349] For all who come of Vánar race Will serve him set in Báli's place. Or else our conquering foes to-day Within our wall will force their way, Polluting with their hostile feet The chambers of thy loved retreat. Great fear is on us, all and one. Those who have wives and who have none, They lust for power, are fierce and bold, Or hate us for the strife of old.” She heard their speech as, sore afraid, Arrested in their flight, they stayed, And gave her answer as became The spirit of so true a dame: “Nay, what have I to do with pelf, With son, with kingdom, or with self, When he, my noble lord, who leads The Vánars like a lion, bleeds? His high-souled victor will I meet, And throw me prostrate at his feet.”
- **Translation**: 

---

### Verse 12 (Ramayana 0.1257)
- **Original**: Canto XIX. Tárá's Grief. 1239 She hastened forth, her bosom rent With anguish, weeping as she went, And striking, mastered by her woes, Her head and breast with frantic blows. She hurried to the field and found Her husband prostrate on the ground, Who quelled the hostile Vánars' might, Whose bank was never turned in flight: Whose arm a massy rock could throw As Indra hurls his bolts below: Fierce as the rushing tempest, loud As thunder from a labouring cloud: Whene'er he roared his voice of fear Struck terror on the boldest ear: Now slain, as, hungry for the prey, A tiger might a lion slay: Or when, his serpent foe to seek, SuparGa600 with his furious beak Tears up a sacred hillock, long The reverence of a village throng, Its altar with their offerings spread, And the gay flag that waved o'erhead. She looked and saw the victor stand Resting upon his bow his hand: And fierce Sugríva she descried, And Lakshma G by his brother's side. She passed them by, nor stayed to view, Swift to her husband's side she flew; Then as she looked, her strength gave way, And in the dust she fell and lay. Then, as if startled ere the close Of slumber, from the earth she rose. 600 A name of Garu a the king of birds, the great enemy of the Serpents.
- **Translation**: 

---

### Verse 13 (Ramayana 0.1258)
- **Original**: 1240 The Ramayana Upon her dying husband, round Whose soul the coils of Death were wound, Her eyes in agony she bent And called him with a shrill lament. Sugríva, when he heard her cries, And saw the queen with weeping eyes, And youthful Angad standing there, His load of grief could hardly bear. Canto XX. Tárá's Lament. Again she bent her to the ground, Her arms about her husband wound. Sobbed on his breast, and sick and faint With anguish poured her wild complaint: “Brave in the charge of battle, boast And glory of the Vánar host, Why on the cold earth wilt thou lie And give no answer when I cry? Up, warrior, from thy lowly bed! A meeter couch for thee is spread. It ill beseems a glorious king On the bare ground his limbs to fling. Ah, surely must thy love be strong For her whom thou hast governed long, If thou, my hero, canst recline On her cold breast forsaking mine. Or, famed for justice through the land, Thou on the road to heaven hast planned Some city fairer far than this To be thy new metropolis.
- **Translation**: 

---

### Verse 14 (Ramayana 0.1259)
- **Original**: Canto XX. Tárá's Lament. 1241 Are all our pleasures ended now, With those delicious hours which thou And I, dear lord, together spent In woods that breathed the honey's scent? Whelmed in my sorrow's boundless sea, There is no joy, no hope, for me, When my beloved lord, who led The Vánars to the fight, is dead, My widowed heart is stern and cold. Or, at the sight mine eyes behold, O'ermastered would it end this ache And in a thousand fragments break. Ah noble Vánar, doomed to pay The penalty of all today— Sugríva from his home expelled, And Rumá 601 from his arms withheld. Our Vánar race and thee to save, Wise counsel for thy weal I gave; But thou, by wildest folly stirred, Wouldst give no credence to my word, And now wilt woo the nymphs above, And shake their souls with pangs of love. Ah, never could it be that thou Beneath Sugríva's power shouldst bow, Thy conqueror is none but Fate Whose mandates all who breathe await. And does no thrill of anguish run Through the stern breast of Raghu's son, Whose base hand dealt a coward's blow, And smote thee fighting with thy foe? Reft of my lord my days, alas! [350] In bitter bitter woe will pass: 601 Sugríva's wife.
- **Translation**: 

---

### Verse 15 (Ramayana 0.1260)
- **Original**: 1242 The Ramayana And I, long blest with every good, Must bear my dreary widowhood. And when his uncle's brow is stern, When his fierce eyes with fury burn, Ah, what will be my Angad's fate, So fair and young and delicate? Come, darling, for the last sad sight, Of thy dear sire who loved the right; For soon thine eyes will long in vain A look at that loved face to gain. And, hero, as thy child draws near, With tender words his spirit cheer; Thy dying wishes gently speak, And kiss him on the brows and cheek. High fame, I ween, has Ráma won By this great deed his hand has done, His debt to brave Sugríva paid And kept the promise that he made. Be happy, King Sugríva, lord Of Ramá to thine arms restored: Enjoy uninterrupted reign, For he, thy foe, at length is slain. Dost thou not hear me speak, and why Hast thou no word of soft reply? Will thou not lift thine eyes and see These dames who look to none but thee?” From their sad eyes, as Tárá spoke, The floods of bitter sorrow broke: Then, pressing close to Angad's side, Each lifted up her voice and cried:
- **Translation**: 

---

### Verse 16 (Ramayana 0.1261)
- **Original**: Canto XXI. Hanumán's Speech. 1243 “How couldst thou leave thine Angad thus, And go, for ever go, from us— Thy child so dear in brave attire, Graced with the virtues of his sire? If e'er in want of thought, O chief, One deed of mine have caused thee grief, Forgive my folly, I entreat, And with my head I touch thy feet.” Again the hapless Tárá wept As to her husband's side she crept, And wild with sorrow and dismay Sat on the ground where Báli lay. Canto XXI. Hanumán's Speech. There, like a fallen star, the dame Fell by her lord's half lifeless frame; And Hanumán drew softly near, And strove her grieving heart to cheer:
- **Translation**: 

---

### Verse 17 (Ramayana 0.1262)
- **Original**: 1244 The Ramayana “By changeless law our bliss and woe From ancient worth and folly flow. What fruits soe'er we cull, the seeds Were scattered by our former deeds.602 Why mourn another's mournful fate, And weep, thyself unfortunate? Be calm, O thou whose heart is wise, For none deserves another's sighs. Look up, with idle sorrow strive: Thy child, his heir, is yet alive. Let needful rites be duly done, Nor in thy woe forget thy son. Regard the law which all obey: They spring to life, they pass away. Begin the task that bids thee rise, And stay these tears, for thou art wise. Our lord the king is doomed to die, On whom ten million hearts rely. Kind, liberal, patient, true, and just Was he in whom they place their trust, And now he seeks the land of those Who for the right subdue their foes. Each Vánar lord with all his train, Each ranger of this wild domain, And Angad here, thy darling, see A governor and friend in thee. These twain603 whose hearts with sorrow ache The funeral rites shall undertake, And Angad by his mother's care Be king, his father's rightful heir. Now let him pay, as laws require, 602 “Our deeds still follow with us from afar. And what we have been makes us what we are.” 603 Sugríva and Angad.
- **Translation**: 

---

### Verse 18 (Ramayana 0.1263)
- **Original**: Canto XXII. Báli Dead. 1245 His sacred duty to his sire, Nor one solemnity omit Of all that mighty kings befit. And when thy fond eye sees thine own Dear Angad on his father's throne, Then, lightened of its load of pain, Thy spirit will have rest again.” She heard his speech, she heaved her head, Looked upon Hanumán and said: “Sweeter my slain lord's limbs to touch, Than Angad or a hundred such. No rule or right, a widowed dame, O'er Angad or the realm I claim. Sugríva is the uncle, he In every act supreme must be. I pray thee, chief, this plan resign, Nor claim from me what ne'er is mine. The father with his tender care Guards the dear child the mother bare, Where'er I be, no sweeter task, No happier joy I hope or ask Than thus to sit with loving eyes And watch the bed where Báli lies. Canto XXII. Báli Dead. There breathing still with slow faint sighs Lay Báli on the ground: his eyes, [351]
- **Translation**: 

---

### Verse 19 (Ramayana 0.1264)
- **Original**: 1246 The Ramayana Damp with the tears of death, he raised, On conquering Sugríva gazed, And then in clearest speech expressed The tender feelings of his breast: “Not to my charge, Sugríva, lay Thine injuries avenged to-day; But rather blame resistless Fate That urged me on infuriate. Fate ne'er agreed our lives to bless With simultaneous happiness: To dwell like brothers side by side In tender love was still denied. The Vánars' realm is thine to-day: Begin, O King, thy rightful sway;604 For I must go at Yáma's call To sojourn in his gloomy hall; Must part and leave this very hour My life, my realm, my kingly power, And go instead of these to gain Bright glory free from spot and stain. Now at thy hands one boon I seek With the last words my lips shall speak, And, though it be no easy thing, Perform the task I give thee, King. This son of mine, no foolish boy, Worthy of bliss and nursed in joy,— See, prostrate on the ground he lies, The hot tears welling from his eyes— The child I love so well, more sweet Than life itself, for woe unmeet,— To him be kindly favour shown: O guard and keep him as thine own. 604 Angad himself, being too young to govern, would be Yuvarája or heir-ap- parent.
- **Translation**: 

---

### Verse 20 (Ramayana 0.1265)
- **Original**: Canto XXII. Báli Dead. 1247 Retain him ever by thy side, His father, helper, friend, and guide. From fear and woe his young life save, And give him all his father gave. Then Tárá's son in time shall be Brave, resolute, and famed like thee, And march before thee to the fight Where stricken fiends shall own his might. While yet a tender stripling, fame Shall bruit abroad his warrior name, And brightly shall his glory shine For exploits worthy of his line. Child of SusheG,605 my Tárá well Obscurest lore can read and tell; And, trained in wondrous art, divines Each mystery of boding signs. Her solemn warning ne'er despise, Do boldly what her lips advise; For things to come her eye can see, And with her words events agree. And for the son of Raghu's sake The toil and danger undertake: For breach of faith were grievous wrong, Nor wouldst thou be unpunished long. Now, brother, take this chain of gold, Gift of celestial hands of old, Or when I die its charm will flee, And all its might be lost with me.” The loving speech Sugríva heard, And all his heart with woe was stirred. Remorse and gentle pity stole Each thought of triumph from his soul: 605 SusheGa was the son of VaruGa the God of the sea.
- **Translation**: 

---

