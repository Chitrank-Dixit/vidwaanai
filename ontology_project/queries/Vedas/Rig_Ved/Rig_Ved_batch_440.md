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

### Verse 1 (Rig Ved 0.8781)
- **Original**: 3814. अग्निस्तुविश्रवस्तमं तुविब्रह्माणपुत्तमम्‌। अतूर्त श्रावयत्पतिं पुत्नं ददाति दाशुषे
- **Translation**: 

---

### Verse 2 (Rig Ved 0.8782)
- **Original**: अग्निदेद हविदाता यजमानों को ऐसा पुत्र दें, जो विविध अत्रों से युक्त, यहुत स्तोत्र करने वाला, उत्तम, अवध्य और उत्तम कर्मों से पूर्वजों का यज्ञ बढ़ाने वाला हो
- **Translation**: 

---

### Verse 3 (Rig Ved 0.8783)
- **Original**: 3815, अम्निर्ददाति सत्पति सासाह यो युथा नृभि: । अग्निरत्यं रघुष्यदं जेतारमपराजितम्‌
- **Translation**: 

---

### Verse 4 (Rig Ved 0.8784)
- **Original**: अभग्निदेव हम लोगों को ऐसा पुत्र दें, जो हमारा साथ देने वाला, शत्रुओं को परास्त करने वाला और सत्यपालक हो । साथ ही अग्निदेव हमें शत्रु-विजेता, अपराजेय, द्रुतगामी अश्व भी प्रदान करें
- **Translation**: 

---

### Verse 5 (Rig Ved 0.8785)
- **Original**: 3816. यद्वाहिष्ठं तदग्नये बृहदर्च विभावसो । महिषीव त्वद्रयिस्त्वद्वाजा उदीरते
- **Translation**: 

---

### Verse 6 (Rig Ved 0.8786)
- **Original**: अभ्निदेव की शीघ्र प्रभावकार स्तोत्रों से स्तुति की जातो है । वे दीप्तिमान्‌ अग्निदेव, हमें अपरिमित धन- धान्य प्रदान करने की कृपा करें
- **Translation**: 

---

### Verse 7 (Rig Ved 0.8787)
- **Original**: 3817 तव द्युमन्तो अर्चयो ग्रावेवोच्यते बृहत्‌। उतो ते तन्यतुर्यथा स्वानो अर्त त्मना दिव:
- **Translation**: 

---

### Verse 8 (Rig Ved 0.8788)
- **Original**: है अग्निदेव ! आपकी शिखायें सर्वत्र दीप्ति से युक्त हैं । आप सोघ्लता कूटने वाले पाषाण की तरह महत्ता से युक्त हैं। आप स्वयं प्रकाश से युक्त हैं । आप प्रेघ-गर्जन के सदृश शब्द से युक्त हैं
- **Translation**: 

---

### Verse 9 (Rig Ved 0.8789)
- **Original**: रद ऋग्वेद संहिता भाग - 2 3818. एवाँ अग्निं वसूयव: सहसान॑ बवन्दिम । स नो विश्वा अति द्विष: पर्षन्नावेव सुक्रतु:
- **Translation**: 

---

### Verse 10 (Rig Ved 0.8790)
- **Original**: हम धन के अभिलाषी मनुष्य बलवान्‌ अग्निदेव की स्तोत्रों से भली प्रकार स्तुति करते हैं। ये उत्तमकर्मा अग्निदेव हम लोगों को शत्रुओं से वैसे ही पार करें, जैसे नाव नदी से पार कर देती है
- **Translation**: 

---

### Verse 11 (Rig Ved 0.8791)
- **Original**: [ सूक्त - 26 ] [ ऋषि - वसूयु आत्रिय
- **Translation**: 

---

### Verse 12 (Rig Ved 0.8792)
- **Original**: देवता - अग्नि; 9 विश्वेदेवा
- **Translation**: 

---

### Verse 13 (Rig Ved 0.8793)
- **Original**: छन्द - गायत्री । 3819. अग्ने पावक रोचिषा मन्द्रया देव जिह्या
- **Translation**: 

---

### Verse 14 (Rig Ved 0.8794)
- **Original**: आ देवान्वक्षि यक्षि च
- **Translation**: 

---

### Verse 15 (Rig Ved 0.8795)
- **Original**: है पवित्रता प्रदान करते वाले अग्निदेव ! देवताओं को प्रसन्न करने वाली ज्वालारूपी जिद्ना द्वारा, देवताओं को आमंत्रित करें और उनके निपित्त यज्ञ सम्पन्न करें
- **Translation**: 

---

### Verse 16 (Rig Ved 0.8796)
- **Original**: 3820. तं त्वा घृतस्नवीमहे चित्रभानो स्वर्दशम्‌
- **Translation**: 

---

### Verse 17 (Rig Ved 0.8797)
- **Original**: देवाँ आ वीतये वह
- **Translation**: 

---

### Verse 18 (Rig Ved 0.8798)
- **Original**: घृत से उत्पन्न होने वाले, अद्भुत तेजस्वों, सबको देखने वाले है अग्ने ! आपको हम प्रार्थना करते हैं । हवि के सेवन के लिए आप देवों को यहाँ बुलायें
- **Translation**: 

---

### Verse 19 (Rig Ved 0.8799)
- **Original**: 3821. बीतिहोत्र॑ त्वा कवे द्युमन्‍्तं समिधीमहि
- **Translation**: 

---

### Verse 20 (Rig Ved 0.8800)
- **Original**: अग्ने बृहन्तमध्यरे
- **Translation**: 

---

