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

### Verse 1 (Ramayan 0.1761)
- **Original**: Canto CXV. Sítá's Joy. 1743 As Raghu's son the rite beheld His loving heart with rapture swelled: But tenderer thoughts within him woke, And thus to Hanúmán he spoke: “Go to my queen: this message give: Say LakshmaG and Sugríva live. The death of Lanká's monarch tell, And bid her joy, for all is well.” Canto CXV. Sítá's Joy. The Vánar chieftain bowed his head, Within the walls of Lanká sped, Leave from the new-made king obtained, And Sítá's lovely garden gained. Beneath a tree the queen he found, Where Rákshas warders watched around. Her pallid cheek, her tangled hair, Her raiment showed her deep despair, Near and more near the envoy came And gently hailed the weeping dame. She started up in sweet surprise, And sudden joy illumed her eyes. For well the Vánar's voice she knew, And hope reviving sprang and grew.
- **Translation**: 

---

### Verse 2 (Ramayan 0.1762)
- **Original**: 1744 The Ramayana “Fair Queen,” he said,“our task is done: The foe is slain and Lanká won. Triumphant mid triumphant friends Kind words of greeting Ráma sends. “Blest for thy sake, O spouse most true, My deadly foe I met and slew. Mine eyes are strangers yet to sleep: I built a bridge athwart the deep And crossed the sea to Lanká's shore To keep the mighty oath I swore. Now, gentle love, thy cares dispel, And weep no more, for all is well. Fear not in RávaG's house to stay For good VibhishaG now bears sway, For constant truth and friendship known Regard his palace as thine own.” He greets thee thus thy heart to cheer, And urged by love will soon be here.” Then flushed with joy the lady's cheek. Her eyes o'erflowed, her voice was weak; But struggling with her sobs she broke Her silence thus, and faintly spoke: “So fast the flood of rapture came, My trembling tongue no words could frame. Ne'er have I heard in days of bliss A tale that gave such joy as this. More precious far than gems and gold The message which thy lips have told.”
- **Translation**: 

---

### Verse 3 (Ramayan 0.1763)
- **Original**: Canto CXV. Sítá's Joy. 1745 His reverent hands the Vánar raised And thus the lady's answer praised: “Sweet are the words, O Queen, which thou True to thy lord, hast spoken now, Better than gems and pearls of price, Yea, or the throne of Paradise. But, lady, ere I leave this place, Grant me, I pray, a single grace. Permit me, and this vengeful hand Shall slay thy guards, this Rákshas band, Whose cruel insult threat and scorn Thy gentle soul too long has borne.” Thus, stern of mood, Hanúmán cried: The Maithil lady thus replied: “Nay, be not wroth with servants: they, When monarchs bid must needs obey. And, vassals of their lords, fulfil Each fancy of their sovereign will. To mine own sins the blame impute, For as we sow we reap the fruit. The tyrant's will these dames obeyed When their fierce threats my soul dismayed.” She ceased: with admiration moved The Vánar chief her words approved: “Thy speech,” he cried,“is worthy one Whom love has linked to Raghu's son. Now speak, O Queen, that I may know Thy pleasure, for to him I go.” The Vánar ceased: then Janak's child Made answer as she sweetly smiled: “'My first, my only wish can be, O chief, my loving lord to see.”
- **Translation**: 

---

### Verse 4 (Ramayan 0.1764)
- **Original**: 1746 The Ramayana Again the Vánar envoy spoke, And with his words new rapture woke: “Queen, ere this sun shall cease to shine Thy Ráma's eyes shall look in thine. Again the lord of Raghu's race Shall turn to thee his moon-bright face. His faithful brother shall thou see And every friend who fought for thee, And greet once more thy king restored LikeZachí1014 to her heavenly lord.” To Raghu's son his steps he bent And told the message that she sent. [495] Canto CXVI. The Meeting. He looked upon that archer chief Whose full eye mocked the lotus leaf, And thus the noble Vánar spake: “Now meet the queen for whose dear sake Thy mighty task was first begun, And now the glorious fruit is won. O'erwhelmed with woe thy lady lies, The hot tears streaming from her eyes. And still the queen must long and pine Until those eyes be turned to thine.” 1014 The consort of Indra.
- **Translation**: 

---

### Verse 5 (Ramayan 0.1765)
- **Original**: Canto CXVI. The Meeting. 1747 But Ráma stood in pensive mood, And gathering tears his eyes bedewed. His sad looks sought the ground: he sighed And thus to King VibhishaG cried: “Let Sítá bathe and tire her head And hither to my sight be led In raiment sweet with precious scent, And gay with golden ornament.” The Rákshas king his palace sought, And Sítá from her bower was brought. Then Rákshas bearers tall and strong, Selected from the menial throng, Through Lanká's gate the queen, arrayed In glorious robes and gems, conveyed. Concealed behind the silken screen, Swift to the plain they bore the queen, While Vánars, close on every side, With eager looks the litter eyed. The warders at VibhishaG's hest The onward rushing throng repressed, While like the roar of ocean loud Rose the wild murmur of the crowd. The son of Raghu saw and moved With anger thus the king reproved: “Why vex with hasty blow and threat The Vánars, and my rights forget? Repress this zeal, untimely shown: I count this people as mine own. A woman's guard is not her bower, The lofty wall, the fenced tower: Her conduct is her best defence, And not a king's magnificence. At holy rites, in war and woe,
- **Translation**: 

---

### Verse 6 (Ramayan 0.1766)
- **Original**: 1748 The Ramayana Her face unveiled a dame may show; When at the Maiden's Choice1015 they meet, When marriage troops parade the street. And she, my queen, who long has lain In prison racked with care and pain, May cease a while her face to hide, For is not Ráma by her side? Lay down the litter: on her feet Let Sítá come her lord to meet. And let the hosts of woodland race Look near upon the lady's face.” Then LakshmaG and each Vánar chief Who heard his words were filled with grief. The lady's gentle spirit sank, And from each eye in fear she shrank, As, her sweet eyelids veiled for shame, Slowly before her lord she came. While rapture battled with surprise She raised to his her wistful eyes. Then with her doubt and fear she strove, And from her breast all sorrow drove. Regardless of the gathering crowd, Bright as the moon without a cloud, She bent her eyes, no longer dim, In joy and trusting love on him. 1015 The Swayamvara, Self-choice or election of a husband by a princess or daughter of a Kshatriya at a public assembly of suitors held for the purpose. For a description of the ceremony seeNala and Damayantían episode of the Mahábhárat translated by the late Dean Milman, andIdylls from the Sanskrit.
- **Translation**: 

---

### Verse 7 (Ramayan 0.1767)
- **Original**: Canto CXVII. Sítá's Disgrace. 1749 Canto CXVII. Sítá's Disgrace. He saw her trembling by his side, And looked upon her face and cried: “Lady, at length my task is done, And thou, the prize of war, art won, This arm my glory has retrieved, And all that man might do achieved; The insulting foe in battle slain And cleared mine honour from its stain. This day has made my name renowned And with success my labour crowned. Lord of myself, the oath I swore Is binding on my soul no more. If from my home my queen was reft, This arm has well avenged the theft, And in the field has wiped away The blot that on mine honour lay. The bridge that spans the foaming flood, The city red with giants' blood; The hosts by King Sugríva led Who wisely counselled, fought and bled; VibhishaG's love, our guide and stay— All these are crowned with fruit to-day. But, lady, 'twas not love for thee That led mine army o'er the sea. 'Twas not for thee our blood was shed, Or Lanká filled with giant dead. No fond affection for my wife Inspired me in the hour of strife. I battled to avenge the cause Of honour and insulted laws. My love is fled, for on thy fame Lies the dark blot of sin and shame;
- **Translation**: 

---

### Verse 8 (Ramayan 0.1768)
- **Original**: 1750 The Ramayana And thou art hateful as the light[496] That flashes on the injured sight. The world is all before thee: flee: Go where thou wilt, but not with me. How should my home receive again A mistress soiled with deathless stain? How should I brook the foul disgrace, Scorned by my friends and all my race? For RávaG bore thee through the sky, And fixed on thine his evil eye. About thy waist his arms he threw, Close to his breast his captive drew, And kept thee, vassal of his power, An inmate of his ladies' bower.” Canto CXVIII. Sítá's Reply. Struck down with overwhelming shame She shrank within her trembling frame. Each word of Ráma's like a dart Had pierced the lady to the heart; And from her sweet eyes unrestrained The torrent of her sorrows, rained. Her weeping eyes at length she dried, And thus mid choking sobs replied: “Canst thou, a high-born prince, dismiss A high-born dame with speech like this? Such words befit the meanest hind, Not princely birth and generous mind, By all my virtuous life I swear I am not what thy words declare.
- **Translation**: 

---

### Verse 9 (Ramayan 0.1769)
- **Original**: Canto CXVIII. Sítá's Reply. 1751 If some are faithless, wilt thou find No love and truth in womankind? Doubt others if thou wilt, but own The truth which all my life has shown. If, when the giant seized his prey, Within his hated arms I lay, And felt the grasp I dreaded, blame Fate and the robber, not thy dame. What could a helpless woman do? My heart was mine and still was true, Why when Hanúmán sent by thee Sought Lanká's town across the sea, Couldst thou not give, O lord of men, Thy sentence of rejection then? Then in the presence of the chief Death, ready death, had brought relief, Nor had I nursed in woe and pain This lingering life, alas in vain. Then hadst thou shunned the fruitless strife Nor jeopardied thy noble life, But spared thy friends and bold allies Their vain and weary enterprise. Is all forgotten, all? my birth, Named Janak's child, from fostering earth? That day of triumph when a maid My trembling hand in thine I laid? My meek obedience to thy will, My faithful love through joy and ill, That never failed at duty's call— O King, is all forgotten, all?” To LakshmaG then she turned and spoke While sobs and sighs her utterance broke: “Sumitrá's son, a pile prepare,
- **Translation**: 

---

### Verse 10 (Ramayan 0.1770)
- **Original**: 1752 The Ramayana My refuge in my dark despair. I will not live to bear this weight Of shame, forlorn and desolate. The kindled fire my woes shall end And be my best and surest friend.” His mournful eyes the hero raised And wistfully on Ráma gazed, In whose stern look no ruth was seen, No mercy for the weeping queen. No chieftain dared to meet those eyes, To pray, to question or advise. The word was passed, the wood was piled And fain to die stood Janak's child. She slowly paced around her lord, The Gods with reverent act adored, Then raising suppliant hands the dame Prayed humbly to the Lord of Flame: “As this fond heart by virtue swayed From Raghu's son has never strayed, So, universal witness, Fire Protect my body on the pyre, As Raghu's son has idly laid This charge on Sítá, hear and aid.” She ceased: and fearless to the last Within the flame's wild fury passed. Then rose a piercing cry from all Dames, children, men, who saw her fall Adorned with gems and gay attire Beneath the fury of the fire.
- **Translation**: 

---

### Verse 11 (Ramayan 0.1771)
- **Original**: Canto CXIX. Glory To Vishnu. 1753 Canto CXIX. Glory To Vishnu. The shrill cry pierced through Ráma's ears And his sad eyes o'erflowed with tears, When lo, transported through the sky A glorious band of Gods was nigh. Ancestral shades,1016 by men revered, In venerable state appeared, And he from whom all riches flow,1017 And Yáma Lord who reigns below: King Indra, thousand-eyed, and he Who wields the sceptre of the sea.1018 The God who shows the blazoned bull,1019 And Brahmá Lord most bountiful By whose command the worlds were made All these on radiant cars conveyed, [497] Brighter than sun-beams, sought the place Where stood the prince of Raghu's race, And from their glittering seats the best Of blessed Gods the chief addressed: “Couldst thou, the Lord of all, couldst thou, Creator of the worlds, allow Thy queen, thy spouse to brave the fire And give her body to the pyre? Dost thou not yet, supremely wise, Thy heavenly nature recognize?” They ceased: and Ráma thus began: “I deem myself a mortal man. Of old Ikshváku's line, I spring 1016 The Pitris or Manes, the spirits of the dead. 1017 Kuvera, the God of Wealth. 1018 VaruG, God of the sea. 1019 Mahádeva orZiva whose ensign is a bull.
- **Translation**: 

---

### Verse 12 (Ramayan 0.1772)
- **Original**: 1754 The Ramayana From Da[aratha Ko[al's king.” He ceased: and Brahmá's self replied: “O cast the idle thought aside. Thou art the Lord NáráyaG, thou The God to whom all creatures bow. Thou art the saviour God who wore Of old the semblance of a boar; Thou he whose discus overthrows All present, past and future foes; Thou Brahmá, That whose days extend Without beginning, growth or end; The God, who, bears the bow of horn, Whom four majestic arms adorn; Thou art the God who rules the sense And sways with gentle influence; Thou all-pervading VishGu Lord Who wears the ever-conquering sword; Thou art the Guide who leads aright, Thou KrishGa of unequalled might. Thy hand, O Lord, the hills and plains, And earth with all her life sustains; Thou wilt appear in serpent form When sinks the earth in fire and storm. Queen Sítá of the lovely brows Is Lakshmí thy celestial spouse. To free the worlds from RávaG thou Wouldst take the form thou wearest now. Rejoice: the mighty task is done: Rejoice, thou great and glorious one. The tyrant, slain, thy labours end: Triumphant now to heaven ascend. High bliss awaits the devotee Who clings in loving faith to thee, Who celebrates with solemn praise
- **Translation**: 

---

### Verse 13 (Ramayan 0.1773)
- **Original**: Canto CXX. Sítá Restored. 1755 The Lord of ne'er beginning days. On earth below, in heaven above Great joy shall crown his faith and love. And he who loves the tale divine Which tells each glorious deed of thine Through life's fair course shall never know The fierce assault of pain and woe.”1020 Canto CXX. Sítá Restored. Thus spoke the Self-existent Sire: Then swiftly from the blazing pyre The circling flames were backward rolled, And, raising in his gentle hold Alive unharmed the Maithil dame, The Lord of Fire embodied came. Fair as the morning was her sheen, And gold and gems adorned the queen. Her form in crimson robes arrayed, Her hair was bound in glossy braid. Her wreath was fresh and sweet of scent, Undimmed was every ornament. Then, standing close to Ráma'a side, The universal witness cried: “From every blot and blemish free Thy faithful queen returns to thee. In word or deed, in look or mind Her heart from thee has ne'er declined. 1020 The Address to Ráma, both text and commentary, will be found literally translated in the Additional Notes. A paraphrase of a portion is all that I have attempted here.
- **Translation**: 

---

### Verse 14 (Ramayan 0.1774)
- **Original**: 1756 The Ramayana By force the giant bore away From thy lone cot his helpless prey; And in his bowers securely kept She still has longed for thee and wept. With soft temptation, bribe and threat, He bade the dame her love forget: But, nobly faithful to her lord, Her soul the giant's suit abhorred. Receive, O King, thy queen again, Pure, ever pure from spot and stain.” Still stood the king in thoughtful mood And tears of joy his eyes bedewed. Then to the best of Gods the best Of warrior chiefs his mind expressed: “'Twas meet that mid the thousands here The searching fire my queen should clear; For long within the giant's bower She dwelt the vassal of his power. For else had many a slanderous tongue Reproaches on mine honour flung, And scorned the king who, love-impelled, His consort from the proof withheld. No doubt had I, but surely knew That Janak's child was pure and true, That, come what might, in good and ill Her faithful heart was with me still. I knew that RávaG could not wrong My queen whom virtue made so strong. I knew his heart would sink and fail, Nor dare her honour to assail, As Ocean, when he raves and roars, Fears to o'erleap his bounding shores.
- **Translation**: 

---

### Verse 15 (Ramayan 0.1775)
- **Original**: Canto CXXI. Dasaratha. 1757 Now to the worlds her truth is shown, And Sítá is again mine own. Thus proved before unnumbered eyes, On her pure fame no shadow lies. As heroes to their glory cleave, Mine own dear spouse I ne'er will leave.” [498] He ceased: and clasped in fond embrace On his dear breast she hid her face. Canto CXXI. Dasaratha. To him Mahe[var thus replied: “O strong-armed hero, lotus-eyed, Thou, best of those who love the right, Hast nobly fought the wondrous fight. Dispelled by thee the doom that spread Through trembling earth and heaven is fled. The worlds exult in light and bliss, And praise thy name, O chief, for this. Now peace to Bharat's heart restore, And bid Kausalyá weep no more. Thy face let Queen Kaikeyí see, Let fond Sumitrá gaze on thee. The longing of thy friends relieve, The kingdom of thy sires receive. Let sons of gentle Sítá born Ikshváku's ancient line adorn. Then from all care and foemen freed Perform the offering of the steed. In pious gifts thy wealth expend, Then to the home of Gods ascend,
- **Translation**: 

---

### Verse 16 (Ramayan 0.1776)
- **Original**: 1758 The Ramayana Thy sire, this glorious king, behold, Among the blest in heaven enrolled. He comes from where the Immortals dwell: Salute him, for he loves thee well.” His mandate Raghu's sons obeyed, And to their sire obeisance made, Where high he stood above the car In wondrous light that shone afar, His limbs in radiant garments dressed Whereon no spot of dust might rest. When on the son he loved so well The eyes of Da[aratha fell, He strained the hero to his breast And thus with gentle words addressed: “No joy to me is heavenly bliss, For there these eyes my Ráma miss. Enrolled on high with saint and sage, Thy woes, dear son, my thoughts engage. Kaikeyí's guile I ne'er forget: Her cruel words will haunt me yet, Which sent thee forth, my son, to roam The forest far from me and home. Now when I look on each dear face, And hold you both in fond embrace, My heart is full of joy to see The sons I love from danger free. Now know I what the Gods designed, And how in Ráma's form enshrined The might of Purushottam lay, The tyrant of the worlds to slay. Ah, how Kausalyá will rejoice To hear again her darling's voice, And, all thy weary wanderings o'er,
- **Translation**: 

---

### Verse 17 (Ramayan 0.1777)
- **Original**: Canto CXXI. Dasaratha. 1759 To gaze upon thy face once more. Ah blest, for ever blest are they Whose eyes shall see the glorious day Of thy return in joy at last, Thy term of toil and exile past. Ayodhyá's lord, begin thy reign, And day by day new glory gain.” He ceased: and Ráma thus replied: “Be not this grace, O sire, denied. Those hasty words, that curse revoke Which from thy lips in anger broke: “Kaikeyí, be no longer mine: I cast thee off, both thee and thine.” O father, let no sorrow fall On her or hers: thy curse recall.” “Yea, she shall live, if so thou wilt,” The sire replied,“absolved from guilt.” Round LakshmaG then his arms he threw, And moved by love began anew: “Great store of merit shall be thine, And brightly shall thy glory shine; Secure on earth thy brother's grace. And high in heaven shall be thy place. Thy glorious king obey and fear: To him the triple world is dear. God, saint, and sage, by Indra led, To Ráma bow the reverent head, Nor from the Lord, the lofty-souled, Their worship or their praise withhold. Heart of the Gods, supreme is he, The One who ne'er shall cease to be.”
- **Translation**: 

---

### Verse 18 (Ramayan 0.1778)
- **Original**: 1760 The Ramayana On Sítá then he looked and smiled; “List to my words” he said,“dear child, Let not thy gentle breast retain One lingering trace of wrath or pain. When by the fire thy truth be proved, By love for thee his will was moved. The furious flame thy faith confessed Which shrank not from the awful test: And thou, in every heart enshrined, Shalt live the best of womankind.” He ceased: he bade the three adieu, And home to heaven exulting flew. Canto CXXII. Indra's Boon. Then Indra, he whose fiery stroke Slew furious Páka, turned and spoke: “A glorious day, O chief, is this, Rich with the fruit of lasting bliss. Well pleased are we: we love thee well Now speak, thy secret wishes tell.”
- **Translation**: 

---

### Verse 19 (Ramayan 0.1779)
- **Original**: Canto CXXII. Indra's Boon. 1761 Thus spake the sovereign of the sky, And this was Ráma's glad reply: “If I have won your grace, incline To grant this one request of mine. Restore, O King: the Vánar dead Whose blood for me was nobly shed.[499] To life and strength my friends recall, And bring them back from Yáma's hall. When, fresh in might the warriors rise, Prepare a feast to glad their eyes. Let fruits of every season glow, And streams of purest water flow.” Thus Raghu's son, great-hearted, prayed, And Indra thus his answer made: “High is the boon thou seekest: none Should win this grace but Raghu's son. Yet, faithful to the word I spake, I grant the prayer for thy dear sake. The Vánars whom the giants slew Their life and vigour shall renew. Their strength repaired, their gashes healed Whose torrents dyed the battle field, The warrior hosts from death shall rise Like sleepers when their slumber flies.” Restored from Yáma's dark domain The Vánar legions filled the plain, And, round the royal chief arrayed, With wondering hearts obeisance paid. Each God the son of Raghu praised, And cried as loud his voice he raised: “Turn, King, to fair Ayodhyá speed, And leave thy friends of Vánar breed.
- **Translation**: 

---

### Verse 20 (Ramayan 0.1780)
- **Original**: 1762 The Ramayana Thy true devoted consort cheer After long days of woe and fear. Bharat, thy loyal brother, see, A hermit now for love of thee. The tears of Queen Kau[alyá dry, And light with joy each stepdame's eye; Then consecrated king of men Make glad each faithful citizen.” They ceased: and borne on radiant cars Sought their bright home amid the stars. Canto CXXIII. The Magic Car. Then slept the tamer of his foes And spent the night in calm repose. VibhishaG came when morning broke, And hailed the royal chief, and spoke: “Here wait thee precious oil and scents, And rich attire and ornaments. The brimming urns are newly filled, And women in their duty skilled, With lotus-eyes, thy call attend, Assistance at thy bath to lend.” “Let others,” Ráma cried,“desire These precious scents, this rich attire, I heed not such delights as these, For faithful Bharat, ill at ease, Watching for me is keeping now Far far away his rigorous vow. By Bharat's side I long to stand,
- **Translation**: 

---

