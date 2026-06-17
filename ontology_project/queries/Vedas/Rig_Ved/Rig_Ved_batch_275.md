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

### Verse 1 (Rig Ved 0.5481)
- **Original**: याज्जिकों के पास नियुत (रथ) में सवार होकर पहुँचने वाले हे वायुदेव ! आपके निमित्त यह देदीप्यमान सोपरस तैयार किया गया है । इस हेतु हम आपका आवाहन करते हैं
- **Translation**: 

---

### Verse 2 (Rig Ved 0.5482)
- **Original**: 60 ऋग्वेद संहिता घाग-1 2411. शुक्रस्थाद्य गवाशिर इन्द्रवायू नियुत्वत:। आ यात॑ पिबतं नरा
- **Translation**: 

---

### Verse 3 (Rig Ved 0.5483)
- **Original**: हे नेतृत्व प्रदान करने वाले इन्द्र और वायुदेवो ! आप आज घोड़ों से युक्त होकर गौ का दूध मिला हुआ तेजस्वी सोमरस पीने के लिए आयें और पान करें
- **Translation**: 

---

### Verse 4 (Rig Ved 0.5484)
- **Original**: 2412.अयं वां मित्रावरुणा सुतः सोम ऋजावृधा। ममेदिह श्रुतं हवम्‌
- **Translation**: 

---

### Verse 5 (Rig Ved 0.5485)
- **Original**: यज्ञ को बढ़ाने वाले हे मित्र और वरुणदेवो ! उत्तम रीति से तैयार एवं शुद्ध किया गया यह सोमरस आपके निमित प्रस्तुत है । हमारी यह प्रार्थना सुनें
- **Translation**: 

---

### Verse 6 (Rig Ved 0.5486)
- **Original**: 2413. राजानावनभिद्ठहा ध्रुवे सदस्युत्तमे। सहस्लस्थुण आसाते
- **Translation**: 

---

### Verse 7 (Rig Ved 0.5487)
- **Original**: आपस में कभी द्रोह न करने वाले हे तेजस्वी पित्र और वरुण देवो ! हजार स्तम्भों पर स्थिर, सशक्त, श्रेष्ठ यज्ञ मण्डप में आप विराजें
- **Translation**: 

---

### Verse 8 (Rig Ved 0.5488)
- **Original**: 2414. ता सप्राजा घृतासुती आदित्या दानुनस्पती
- **Translation**: 

---

### Verse 9 (Rig Ved 0.5489)
- **Original**: सचेते अनवह्नरम्‌
- **Translation**: 

---

### Verse 10 (Rig Ved 0.5490)
- **Original**: सम्राट्‌ रूप, घृताहुति स्वीकार करने वाले, दानशील अदिति पुत्र मित्र और वरुणदेव, कुटिलता से रहित (सरल हृदय वाले) , साधकों (याजकों) की ही सहायता करते हैं
- **Translation**: 

---

### Verse 11 (Rig Ved 0.5491)
- **Original**: 2415. गोमदू घु नासत्याश्रावद्यातमश्चिना । वर्ती रुद्रा नूपाय्यम्‌
- **Translation**: 

---

### Verse 12 (Rig Ved 0.5492)
- **Original**: हे अश्विनीकुमारों ! हे सत्य सेवी रुद्रदेवो ! जिस सोघरस का पान यज् में नेतृत्व प्रदान करने वाले लोग करेंगे, उस सोमरस को गौओं तथा अश्षों से युक्त रथ में आप भली-भाँति लाये
- **Translation**: 

---

### Verse 13 (Rig Ved 0.5493)
- **Original**: 2416. न यत्परोनान्तर आदधर्षद्वृषण्वसू। दुःशंसो मत्यों रिपुः
- **Translation**: 

---

### Verse 14 (Rig Ved 0.5494)
- **Original**: हे धनवर्षक अश्विनीकुमारो ! समीप में रहनेवाले या दूर रहने वाले कटुभाषी शत्रु जिस धन को नहीं चुरा सकते, उसे हमें प्रदान करें
- **Translation**: 

---

### Verse 15 (Rig Ved 0.5495)
- **Original**: 2417. ता न आ योल्हहमश्विना रयिं पिशड्रसन्दशम्‌। धिष्ण्या वरिवोविदम्‌
- **Translation**: 

---

### Verse 16 (Rig Ved 0.5496)
- **Original**: हे उत्तम स्तुति के योग्य अश्विनीकुमारो ! आपके पास्त जो सुवर्णयुक्त नाना प्रकार का ऐश्वर्य है, वह धन हमारे लिए ले आये
- **Translation**: 

---

### Verse 17 (Rig Ved 0.5497)
- **Original**: 2418. इन्द्रो अड़ महद्धयमभी षदप चुच्यवत्‌। स हि स्थिरो विचर्षणि:
- **Translation**: 

---

### Verse 18 (Rig Ved 0.5498)
- **Original**: युद्ध में स्थिर रहने वाले विश्वद्रष्टा इन्द्रदेव महान्‌ पराधवकारी भय को शौघ्र ही दूर करते हैं
- **Translation**: 

---

### Verse 19 (Rig Ved 0.5499)
- **Original**: 2419. इुद्धक्न मृछयाति नो न न: पश्चादघ नशत्‌ । भद्र भवाति नः पुर:
- **Translation**: 

---

### Verse 20 (Rig Ved 0.5500)
- **Original**: किक यदि इद्धदेव हमें सुखप्रदान करेंगे, तो हमें पाप नष्ट नहीं कर सकता, वे हर प्रकार से हमारा कल्याण ही
- **Translation**: 

---

