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

### Verse 1 (Ramayana 0.1766)
- **Original**: 1748 The Ramayana Her face unveiled a dame may show; When at the Maiden's Choice1015 they meet, When marriage troops parade the street. And she, my queen, who long has lain In prison racked with care and pain, May cease a while her face to hide, For is not Ráma by her side? Lay down the litter: on her feet Let Sítá come her lord to meet. And let the hosts of woodland race Look near upon the lady's face.” Then LakshmaG and each Vánar chief Who heard his words were filled with grief. The lady's gentle spirit sank, And from each eye in fear she shrank, As, her sweet eyelids veiled for shame, Slowly before her lord she came. While rapture battled with surprise She raised to his her wistful eyes. Then with her doubt and fear she strove, And from her breast all sorrow drove. Regardless of the gathering crowd, Bright as the moon without a cloud, She bent her eyes, no longer dim, In joy and trusting love on him. 1015 The Swayamvara, Self-choice or election of a husband by a princess or daughter of a Kshatriya at a public assembly of suitors held for the purpose. For a description of the ceremony seeNala and Damayantían episode of the Mahábhárat translated by the late Dean Milman, andIdylls from the Sanskrit.
- **Translation**: 

---

### Verse 2 (Ramayana 0.1767)
- **Original**: Canto CXVII. Sítá's Disgrace. 1749 Canto CXVII. Sítá's Disgrace. He saw her trembling by his side, And looked upon her face and cried: “Lady, at length my task is done, And thou, the prize of war, art won, This arm my glory has retrieved, And all that man might do achieved; The insulting foe in battle slain And cleared mine honour from its stain. This day has made my name renowned And with success my labour crowned. Lord of myself, the oath I swore Is binding on my soul no more. If from my home my queen was reft, This arm has well avenged the theft, And in the field has wiped away The blot that on mine honour lay. The bridge that spans the foaming flood, The city red with giants' blood; The hosts by King Sugríva led Who wisely counselled, fought and bled; VibhishaG's love, our guide and stay— All these are crowned with fruit to-day. But, lady, 'twas not love for thee That led mine army o'er the sea. 'Twas not for thee our blood was shed, Or Lanká filled with giant dead. No fond affection for my wife Inspired me in the hour of strife. I battled to avenge the cause Of honour and insulted laws. My love is fled, for on thy fame Lies the dark blot of sin and shame;
- **Translation**: 

---

### Verse 3 (Ramayana 0.1768)
- **Original**: 1750 The Ramayana And thou art hateful as the light[496] That flashes on the injured sight. The world is all before thee: flee: Go where thou wilt, but not with me. How should my home receive again A mistress soiled with deathless stain? How should I brook the foul disgrace, Scorned by my friends and all my race? For RávaG bore thee through the sky, And fixed on thine his evil eye. About thy waist his arms he threw, Close to his breast his captive drew, And kept thee, vassal of his power, An inmate of his ladies' bower.” Canto CXVIII. Sítá's Reply. Struck down with overwhelming shame She shrank within her trembling frame. Each word of Ráma's like a dart Had pierced the lady to the heart; And from her sweet eyes unrestrained The torrent of her sorrows, rained. Her weeping eyes at length she dried, And thus mid choking sobs replied: “Canst thou, a high-born prince, dismiss A high-born dame with speech like this? Such words befit the meanest hind, Not princely birth and generous mind, By all my virtuous life I swear I am not what thy words declare.
- **Translation**: 

---

### Verse 4 (Ramayana 0.1769)
- **Original**: Canto CXVIII. Sítá's Reply. 1751 If some are faithless, wilt thou find No love and truth in womankind? Doubt others if thou wilt, but own The truth which all my life has shown. If, when the giant seized his prey, Within his hated arms I lay, And felt the grasp I dreaded, blame Fate and the robber, not thy dame. What could a helpless woman do? My heart was mine and still was true, Why when Hanúmán sent by thee Sought Lanká's town across the sea, Couldst thou not give, O lord of men, Thy sentence of rejection then? Then in the presence of the chief Death, ready death, had brought relief, Nor had I nursed in woe and pain This lingering life, alas in vain. Then hadst thou shunned the fruitless strife Nor jeopardied thy noble life, But spared thy friends and bold allies Their vain and weary enterprise. Is all forgotten, all? my birth, Named Janak's child, from fostering earth? That day of triumph when a maid My trembling hand in thine I laid? My meek obedience to thy will, My faithful love through joy and ill, That never failed at duty's call— O King, is all forgotten, all?” To LakshmaG then she turned and spoke While sobs and sighs her utterance broke: “Sumitrá's son, a pile prepare,
- **Translation**: 

---

### Verse 5 (Ramayana 0.1770)
- **Original**: 1752 The Ramayana My refuge in my dark despair. I will not live to bear this weight Of shame, forlorn and desolate. The kindled fire my woes shall end And be my best and surest friend.” His mournful eyes the hero raised And wistfully on Ráma gazed, In whose stern look no ruth was seen, No mercy for the weeping queen. No chieftain dared to meet those eyes, To pray, to question or advise. The word was passed, the wood was piled And fain to die stood Janak's child. She slowly paced around her lord, The Gods with reverent act adored, Then raising suppliant hands the dame Prayed humbly to the Lord of Flame: “As this fond heart by virtue swayed From Raghu's son has never strayed, So, universal witness, Fire Protect my body on the pyre, As Raghu's son has idly laid This charge on Sítá, hear and aid.” She ceased: and fearless to the last Within the flame's wild fury passed. Then rose a piercing cry from all Dames, children, men, who saw her fall Adorned with gems and gay attire Beneath the fury of the fire.
- **Translation**: 

---

### Verse 6 (Ramayana 0.1771)
- **Original**: Canto CXIX. Glory To Vishnu. 1753 Canto CXIX. Glory To Vishnu. The shrill cry pierced through Ráma's ears And his sad eyes o'erflowed with tears, When lo, transported through the sky A glorious band of Gods was nigh. Ancestral shades,1016 by men revered, In venerable state appeared, And he from whom all riches flow,1017 And Yáma Lord who reigns below: King Indra, thousand-eyed, and he Who wields the sceptre of the sea.1018 The God who shows the blazoned bull,1019 And Brahmá Lord most bountiful By whose command the worlds were made All these on radiant cars conveyed, [497] Brighter than sun-beams, sought the place Where stood the prince of Raghu's race, And from their glittering seats the best Of blessed Gods the chief addressed: “Couldst thou, the Lord of all, couldst thou, Creator of the worlds, allow Thy queen, thy spouse to brave the fire And give her body to the pyre? Dost thou not yet, supremely wise, Thy heavenly nature recognize?” They ceased: and Ráma thus began: “I deem myself a mortal man. Of old Ikshváku's line, I spring 1016 The Pitris or Manes, the spirits of the dead. 1017 Kuvera, the God of Wealth. 1018 VaruG, God of the sea. 1019 Mahádeva orZiva whose ensign is a bull.
- **Translation**: 

---

### Verse 7 (Ramayana 0.1772)
- **Original**: 1754 The Ramayana From Da[aratha Ko[al's king.” He ceased: and Brahmá's self replied: “O cast the idle thought aside. Thou art the Lord NáráyaG, thou The God to whom all creatures bow. Thou art the saviour God who wore Of old the semblance of a boar; Thou he whose discus overthrows All present, past and future foes; Thou Brahmá, That whose days extend Without beginning, growth or end; The God, who, bears the bow of horn, Whom four majestic arms adorn; Thou art the God who rules the sense And sways with gentle influence; Thou all-pervading VishGu Lord Who wears the ever-conquering sword; Thou art the Guide who leads aright, Thou KrishGa of unequalled might. Thy hand, O Lord, the hills and plains, And earth with all her life sustains; Thou wilt appear in serpent form When sinks the earth in fire and storm. Queen Sítá of the lovely brows Is Lakshmí thy celestial spouse. To free the worlds from RávaG thou Wouldst take the form thou wearest now. Rejoice: the mighty task is done: Rejoice, thou great and glorious one. The tyrant, slain, thy labours end: Triumphant now to heaven ascend. High bliss awaits the devotee Who clings in loving faith to thee, Who celebrates with solemn praise
- **Translation**: 

---

### Verse 8 (Ramayana 0.1773)
- **Original**: Canto CXX. Sítá Restored. 1755 The Lord of ne'er beginning days. On earth below, in heaven above Great joy shall crown his faith and love. And he who loves the tale divine Which tells each glorious deed of thine Through life's fair course shall never know The fierce assault of pain and woe.”1020 Canto CXX. Sítá Restored. Thus spoke the Self-existent Sire: Then swiftly from the blazing pyre The circling flames were backward rolled, And, raising in his gentle hold Alive unharmed the Maithil dame, The Lord of Fire embodied came. Fair as the morning was her sheen, And gold and gems adorned the queen. Her form in crimson robes arrayed, Her hair was bound in glossy braid. Her wreath was fresh and sweet of scent, Undimmed was every ornament. Then, standing close to Ráma'a side, The universal witness cried: “From every blot and blemish free Thy faithful queen returns to thee. In word or deed, in look or mind Her heart from thee has ne'er declined. 1020 The Address to Ráma, both text and commentary, will be found literally translated in the Additional Notes. A paraphrase of a portion is all that I have attempted here.
- **Translation**: 

---

### Verse 9 (Ramayana 0.1774)
- **Original**: 1756 The Ramayana By force the giant bore away From thy lone cot his helpless prey; And in his bowers securely kept She still has longed for thee and wept. With soft temptation, bribe and threat, He bade the dame her love forget: But, nobly faithful to her lord, Her soul the giant's suit abhorred. Receive, O King, thy queen again, Pure, ever pure from spot and stain.” Still stood the king in thoughtful mood And tears of joy his eyes bedewed. Then to the best of Gods the best Of warrior chiefs his mind expressed: “'Twas meet that mid the thousands here The searching fire my queen should clear; For long within the giant's bower She dwelt the vassal of his power. For else had many a slanderous tongue Reproaches on mine honour flung, And scorned the king who, love-impelled, His consort from the proof withheld. No doubt had I, but surely knew That Janak's child was pure and true, That, come what might, in good and ill Her faithful heart was with me still. I knew that RávaG could not wrong My queen whom virtue made so strong. I knew his heart would sink and fail, Nor dare her honour to assail, As Ocean, when he raves and roars, Fears to o'erleap his bounding shores.
- **Translation**: 

---

### Verse 10 (Ramayana 0.1775)
- **Original**: Canto CXXI. Dasaratha. 1757 Now to the worlds her truth is shown, And Sítá is again mine own. Thus proved before unnumbered eyes, On her pure fame no shadow lies. As heroes to their glory cleave, Mine own dear spouse I ne'er will leave.” [498] He ceased: and clasped in fond embrace On his dear breast she hid her face. Canto CXXI. Dasaratha. To him Mahe[var thus replied: “O strong-armed hero, lotus-eyed, Thou, best of those who love the right, Hast nobly fought the wondrous fight. Dispelled by thee the doom that spread Through trembling earth and heaven is fled. The worlds exult in light and bliss, And praise thy name, O chief, for this. Now peace to Bharat's heart restore, And bid Kausalyá weep no more. Thy face let Queen Kaikeyí see, Let fond Sumitrá gaze on thee. The longing of thy friends relieve, The kingdom of thy sires receive. Let sons of gentle Sítá born Ikshváku's ancient line adorn. Then from all care and foemen freed Perform the offering of the steed. In pious gifts thy wealth expend, Then to the home of Gods ascend,
- **Translation**: 

---

### Verse 11 (Ramayana 0.1776)
- **Original**: 1758 The Ramayana Thy sire, this glorious king, behold, Among the blest in heaven enrolled. He comes from where the Immortals dwell: Salute him, for he loves thee well.” His mandate Raghu's sons obeyed, And to their sire obeisance made, Where high he stood above the car In wondrous light that shone afar, His limbs in radiant garments dressed Whereon no spot of dust might rest. When on the son he loved so well The eyes of Da[aratha fell, He strained the hero to his breast And thus with gentle words addressed: “No joy to me is heavenly bliss, For there these eyes my Ráma miss. Enrolled on high with saint and sage, Thy woes, dear son, my thoughts engage. Kaikeyí's guile I ne'er forget: Her cruel words will haunt me yet, Which sent thee forth, my son, to roam The forest far from me and home. Now when I look on each dear face, And hold you both in fond embrace, My heart is full of joy to see The sons I love from danger free. Now know I what the Gods designed, And how in Ráma's form enshrined The might of Purushottam lay, The tyrant of the worlds to slay. Ah, how Kausalyá will rejoice To hear again her darling's voice, And, all thy weary wanderings o'er,
- **Translation**: 

---

### Verse 12 (Ramayana 0.1777)
- **Original**: Canto CXXI. Dasaratha. 1759 To gaze upon thy face once more. Ah blest, for ever blest are they Whose eyes shall see the glorious day Of thy return in joy at last, Thy term of toil and exile past. Ayodhyá's lord, begin thy reign, And day by day new glory gain.” He ceased: and Ráma thus replied: “Be not this grace, O sire, denied. Those hasty words, that curse revoke Which from thy lips in anger broke: “Kaikeyí, be no longer mine: I cast thee off, both thee and thine.” O father, let no sorrow fall On her or hers: thy curse recall.” “Yea, she shall live, if so thou wilt,” The sire replied,“absolved from guilt.” Round LakshmaG then his arms he threw, And moved by love began anew: “Great store of merit shall be thine, And brightly shall thy glory shine; Secure on earth thy brother's grace. And high in heaven shall be thy place. Thy glorious king obey and fear: To him the triple world is dear. God, saint, and sage, by Indra led, To Ráma bow the reverent head, Nor from the Lord, the lofty-souled, Their worship or their praise withhold. Heart of the Gods, supreme is he, The One who ne'er shall cease to be.”
- **Translation**: 

---

### Verse 13 (Ramayana 0.1778)
- **Original**: 1760 The Ramayana On Sítá then he looked and smiled; “List to my words” he said,“dear child, Let not thy gentle breast retain One lingering trace of wrath or pain. When by the fire thy truth be proved, By love for thee his will was moved. The furious flame thy faith confessed Which shrank not from the awful test: And thou, in every heart enshrined, Shalt live the best of womankind.” He ceased: he bade the three adieu, And home to heaven exulting flew. Canto CXXII. Indra's Boon. Then Indra, he whose fiery stroke Slew furious Páka, turned and spoke: “A glorious day, O chief, is this, Rich with the fruit of lasting bliss. Well pleased are we: we love thee well Now speak, thy secret wishes tell.”
- **Translation**: 

---

### Verse 14 (Ramayana 0.1779)
- **Original**: Canto CXXII. Indra's Boon. 1761 Thus spake the sovereign of the sky, And this was Ráma's glad reply: “If I have won your grace, incline To grant this one request of mine. Restore, O King: the Vánar dead Whose blood for me was nobly shed.[499] To life and strength my friends recall, And bring them back from Yáma's hall. When, fresh in might the warriors rise, Prepare a feast to glad their eyes. Let fruits of every season glow, And streams of purest water flow.” Thus Raghu's son, great-hearted, prayed, And Indra thus his answer made: “High is the boon thou seekest: none Should win this grace but Raghu's son. Yet, faithful to the word I spake, I grant the prayer for thy dear sake. The Vánars whom the giants slew Their life and vigour shall renew. Their strength repaired, their gashes healed Whose torrents dyed the battle field, The warrior hosts from death shall rise Like sleepers when their slumber flies.” Restored from Yáma's dark domain The Vánar legions filled the plain, And, round the royal chief arrayed, With wondering hearts obeisance paid. Each God the son of Raghu praised, And cried as loud his voice he raised: “Turn, King, to fair Ayodhyá speed, And leave thy friends of Vánar breed.
- **Translation**: 

---

### Verse 15 (Ramayana 0.1780)
- **Original**: 1762 The Ramayana Thy true devoted consort cheer After long days of woe and fear. Bharat, thy loyal brother, see, A hermit now for love of thee. The tears of Queen Kau[alyá dry, And light with joy each stepdame's eye; Then consecrated king of men Make glad each faithful citizen.” They ceased: and borne on radiant cars Sought their bright home amid the stars. Canto CXXIII. The Magic Car. Then slept the tamer of his foes And spent the night in calm repose. VibhishaG came when morning broke, And hailed the royal chief, and spoke: “Here wait thee precious oil and scents, And rich attire and ornaments. The brimming urns are newly filled, And women in their duty skilled, With lotus-eyes, thy call attend, Assistance at thy bath to lend.” “Let others,” Ráma cried,“desire These precious scents, this rich attire, I heed not such delights as these, For faithful Bharat, ill at ease, Watching for me is keeping now Far far away his rigorous vow. By Bharat's side I long to stand,
- **Translation**: 

---

### Verse 16 (Ramayana 0.1781)
- **Original**: Canto CXXIII. The Magic Car. 1763 I long to see my fatherland. Far is Ayodhyá: long, alas, The dreary road and hard to pass.” “One day,” VibhishaG cried,“one day Shall bear thee o'er that length of way. Is not the wondrous chariot mine, Named Pushpak, wrought by hands divine. The prize which RávaG seized of old Victorious o'er the God of Gold? This chariot, kept with utmost care, Will waft thee through the fields of air, And thou shalt light unwearied down In fair Ayodhyá's royal town. But yet if aught that I have done Has pleased thee well, O Raghu's son; If still thou carest for thy friend, Some little time in Lanká spend; There after toil of battle rest Within my halls an honoured guest.” Again the son of Raghu spake: “Thy life was perilled for my sake. Thy counsel gave me priceless aid: All honours have been richly paid. Scarce can my love refuse, O best Of giant kind, thy last request. But still I yearn once more to see My home and all most dear to me; Nor can I brook one hour's delay: Forgive me, speed me on my way.” He ceased: the magic car was brought. Of yore by Vi[vakarmá wrought. In sunlike sheen it flashed and blazed; And Raghu's sons in wonder gazed.
- **Translation**: 

---

### Verse 17 (Ramayana 0.1782)
- **Original**: 1764 The Ramayana Canto CXXIV. The Departure. The giant lord the chariot viewed, And humbly thus his speech renewed: “Behold, O King, the car prepared: Now be thy further will declared.” He ceased: and Ráma spake once more: “These hosts who thronged to Lanká's shore Their faith and might have nobly shown, And set thee on the giants' throne. Let pearls and gems and gold repay The feats of many a desperate day, That all may go triumphant hence Proud of their noble recompense.” VibhishaG, ready at his call, With gold and gems enriched them all. Then Ráma clomb the glorious car That shone like day's resplendent star. There in his lap he held his dame Vailing her eyes in modest shame. Beside him LakshmaG took his stand, Whose mighty bow still armed his hand, “O King VibhishaG,” Ráma cried, “O Vánar chiefs, so long allied,[500] My comrades till the foemen fell, List, for I speak a long farewell. The task, in doubt and fear begun, With your good aid is nobly done. Leave Lanká's shore, your steps retrace, Brave warriors of the Vánar race. Thou, King Sugríva, true, through all, To friendship's bond and duty's call, Seek far Kishkindhá with thy train And o'er thy realm in glory reign.
- **Translation**: 

---

### Verse 18 (Ramayana 0.1783)
- **Original**: Canto CXXIV. The Departure. 1765 Farewell, VibhishaG, Lanká's throne Won by our arms is now thine own, Thou, mighty lord, hast nought to dread From heavenly Gods by Indra led. My last farewell, 0 King, receive, For Lanká's isle this hour I leave.” Loud rose their cry in answer:“We, O Raghu's son, would go with thee. With thee delighted would we stray Where sweet Ayodhyá's groves are gay, Then in the joyous synod view King-making balm thy brows bedew; Our homage to Kau[alyá pay, And hasten on our homeward way.” Their prayer the son of Raghu heard, And spoke, his heart with rapture stirred: “Sugríva, O my faithful friend, VibhishaG and ye chiefs, ascend. A joy beyond all joys the best Will fill my overflowing breast, If girt by you, O noble band, I seek again my native land.” With Vánar lords in danger tried Sugríva sprang to Ráma's side, And girt by chiefs of giant kind Vibhíshan's step was close behind. Swift through the air, as Ráma chose, The wondrous car from earth arose. And decked with swans and silver wings Bore through the clouds its freight of kings.
- **Translation**: 

---

### Verse 19 (Ramayana 0.1784)
- **Original**: 1766 The Ramayana Canto CXXV. The Return. Then Ráma, speeding through the skies, Bent on the earth his eager eyes: “Look, Sítá, see, divinely planned And built by Vi[vakarmá's hand, Lanká the lovely city rest Enthroned on Mount Trikúma's crest Behold those fields, ensanguined yet, Where Vánar hosts and giants met. There, vainly screened by charm and spell, The robber Rávan fought and fell. There knelt Mandodarí1021 and shed Her tears in floods for Rávan dead. And every dame who loved him sent From her sad heart her wild lament. There gleams the margin of the deep, Where, worn with toil, we sank to sleep. Look, love, the unconquered sea behold, King VaruG's home ordained of old, Whose boundless waters roar and swell Rich with their store of pearl and shell. O see, the morning sun is bright On fair HiraGyanábha's1022 height, Who rose from Ocean's sheltering breast That Hanumán might stay and rest. There stretches, famed for evermore, The wondrous bridge from shore to shore. The worlds, to life's remotest day, Due reverence to the work shall pay, Which holier for the lapse of time 1021 RávaG's queen. 1022 Or Maináka.
- **Translation**: 

---

### Verse 20 (Ramayana 0.1785)
- **Original**: Canto CXXV. The Return. 1767 Shall give release from sin and crime. Now thither bend, dear love, thine eyes Where green with groves Kishkindhá lies, The seat of King Sugríva's reign, Where Báli by this hand was slain.1023 There Ríshyamúka's hill behold Bright gleaming with embedded gold. There too my wandering foot I set, There King Sugríva first I met. And, where yon trees their branches wave, My promise of assistance gave. There, flushed with lilies, Pampá shines With banks which greenest foliage lines, Where melancholy steps I bent And mourned thee with a mad lament. There fierce Kabandha, spreading wide His giant arms, in battle died. Turn, Sítá, turn thine eyes and see In Janasthán that glorious tree: There RávaG, lord of giants slew Our friend Jamáyus brave and true, Thy champion in the hopeless strife, Who gave for thee his noble life. Now mark that glade amid the trees Where once we lived as devotees. See, see our leafy cot between Those waving boughs of densest green, Where RávaG seized his prize and stole My love the darling of my soul. O, look again: beneath thee gleams 1023 Here, in the North-west recension, Sítá expresses a wish that Tárá and the wives of the Vánar chiefs should be invited to accompany her to Ayodhyá. The car decends, and the Vánar matrons are added to the party. The Bengal recension ignores this palpable interruption.
- **Translation**: 

---

