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

### Verse 1 (Rig Ved 0.8161)
- **Original**: है बायु और इद्धदेवो ! आप दोनों सोमपान की पात्रता से युक्त हैं, इसोलिए नीचे की ओर जलधारा के समान ही आप दोनों तक सोमरस के प्रवाह पहुँचते हैं
- **Translation**: 

---

### Verse 2 (Rig Ved 0.8162)
- **Original**: 3551. वायबिन्द्रश्व शुध्पिणा सरथं शवसस्पती । नियुत्वन्ता न ऊतय आ थात॑ सोमपीतये
- **Translation**: 

---

### Verse 3 (Rig Ved 0.8163)
- **Original**: हे वायु और इन्धदेवो ! आप दोनों बल के स्वामी और सामर्थ्यवान्‌ हैं। नियुत नामक घोड़े से युक्त आप
- **Translation**: 

---

### Verse 4 (Rig Ved 0.8164)
- **Original**: छ्ड ऋग्वेद संहिता भाग - 2 दोनों ही हमारी रक्षा के लिए सोमरस पान हेतु एक साथ पधारें
- **Translation**: 

---

### Verse 5 (Rig Ved 0.8165)
- **Original**: 3552. या वां सन्ति पुरुस्पृहो नियुतो दाशुषे नरा। अस्मे ता यज्ञवाहसेन्द्रवायू नि यच्छतम्‌
- **Translation**: 

---

### Verse 6 (Rig Ved 0.8166)
- **Original**: हे नायक तथा यज्ञ सम्पादक इन्द्र और बायुदेवो ! आप दोनों के पास अनेकों द्रारा कामना किये जाने योग्य जो अश्च हैं, उन अश्ों को मुझ दानदाता यजमान को प्रदान करें
- **Translation**: 

---

### Verse 7 (Rig Ved 0.8167)
- **Original**: सूक्त - 48
- **Translation**: 

---

### Verse 8 (Rig Ved 0.8168)
- **Original**: ऋषि - वामदेव गौतम । देवता - वायु । छन्द - अनुश्टप्‌ ।
- **Translation**: 

---

### Verse 9 (Rig Ved 0.8169)
- **Original**: 3553. बिहि होत्रा अवीता विपो न रायो अर्य:। वायवा चन्द्रेण रथेन याहि सुतस्य पीतये
- **Translation**: 

---

### Verse 10 (Rig Ved 0.8170)
- **Original**: हे वायुदेव ! रिपुओं को प्रकम्पित करने वाले योद्धा की तरह अन्यों के द्वारा न पिये गये सोमरस का आप पान करें तथा स्तोताओं के ऐश्वर्य की वृद्धि करें
- **Translation**: 

---

### Verse 11 (Rig Ved 0.8171)
- **Original**: हे वायुदेव ! आप सोमरस पौने के लिए शौतलतादायक रथ द्वारा आगमन करें
- **Translation**: 

---

### Verse 12 (Rig Ved 0.8172)
- **Original**: 3554 निर्युवाणो अशस्तीर्नियुत्याँ इन्द्रसारथि: । वायवा चद्देण रथेन याहि सुतस्य पीतये
- **Translation**: 

---

### Verse 13 (Rig Ved 0.8173)
- **Original**: हे वायुदेय ! आप वर्णन न किये जाने योग्य, तरुणता से युक्त अश्वों क्यो नियोजित करते हैं । इन्द्रदेवता आपके सारथि हैं
- **Translation**: 

---

### Verse 14 (Rig Ved 0.8174)
- **Original**: हे वायुदेव ! आप सोमरस पीने के लिए तेजस्वी रथ द्वारा पधारें
- **Translation**: 

---

### Verse 15 (Rig Ved 0.8175)
- **Original**: 3555. अनु कृष्णे बसुधिती येमाते विश्वपेशसा । वायवा चन्द्रेण रथेन याहि सुतस्य पीतये
- **Translation**: 

---

### Verse 16 (Rig Ved 0.8176)
- **Original**: हे वायुदेव ! काले रंगों वाली, ऐश्वर्यों को धारण करने वाली, बहुत रूपों वाली द्यावा-पृथिवी आपका ही अनुगमन करती हैं। आप सोमरस पान के निमित्त तेजस्वी रथ द्वारा पथारें
- **Translation**: 

---

### Verse 17 (Rig Ved 0.8177)
- **Original**: 3556. वहन्तु त्वा मनोयुजो युक्तासो नवतिर्नव वायवा चन्द्रेण रथेन याहि सुतस्य पीतये
- **Translation**: 

---

### Verse 18 (Rig Ved 0.8178)
- **Original**: है वायुदेव ! मन के समान वेग वाले, परस्पर नियोजित होने वाले निन्‍्यानवे घोड़े आपको ले जाते हैं । हे वायुदेव ! आप तेजस्वी रथ द्वारा सोमपान के निमित्त पधारें
- **Translation**: 

---

### Verse 19 (Rig Ved 0.8179)
- **Original**: 3557, वायो शतं हरीणां युवस्व पोष्याणाम्‌ । उत वा ते सहर्रिणो रथ आ यातु पाजसा
- **Translation**: 

---

### Verse 20 (Rig Ved 0.8180)
- **Original**: हे बायुदेव
- **Translation**: 

---

