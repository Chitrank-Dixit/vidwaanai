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

### Verse 1 (Rig Ved 0.21)
- **Original**: हे देव ! हमें आपका सानिध्य प्राप्त हो
- **Translation**: 

---

### Verse 2 (Rig Ved 0.22)
- **Original**: 8. राजन्तमध्वराणां गोपामृतस्थ दीदिविम्‌। वर्धमानं स्वे दमे
- **Translation**: 

---

### Verse 3 (Rig Ved 0.23)
- **Original**: हम गृहस्थ लोग दोप्तिमान्‌ , यज्ञों के रक्षक, सत्यवचनरूप व्रत को आलोकित करने वाले, यज्ञस्थल में वृद्धि को आ्प्त करने वाले अग्निदेव के निकट स्तुतिपूर्वक आते हैं
- **Translation**: 

---

### Verse 4 (Rig Ved 0.24)
- **Original**: 9. स नः पितेव सूनवे5ग्ने सूपायनो भव। सचस्वा नः स्वस्तये
- **Translation**: 

---

### Verse 5 (Rig Ved 0.25)
- **Original**: हे गार्पत्य अग्ने ! जिस प्रकार पुत्र को पिता (बिना बाधा के) सहज़ ही प्राप्त होता है, उसी प्रकार आप भी (हम यजमानों के लिये) बाधारहित होकर सुखपूर्वक प्राप्त हों । आप हमारे कल्याण के लये हमारे निकट रहें
- **Translation**: 

---

### Verse 6 (Rig Ved 0.26)
- **Original**: [ सूक्त - 2
- **Translation**: 

---

### Verse 7 (Rig Ved 0.27)
- **Original**: [ऋषि -मधुच्छन्दा वैश्वामित्र । देवता-1-3 वायु 4-6-इन्द्र-बायु ; 7-9 भित्रावरुण
- **Translation**: 

---

### Verse 8 (Rig Ved 0.28)
- **Original**: छत्द-गायत्री ।] 10, वायवा याहि दर्शतेमे सोमा अरंकृता:। तेषां पाहि श्रुधी हवम्‌
- **Translation**: 

---

### Verse 9 (Rig Ved 0.29)
- **Original**: है प्रियदर्शी बायुदेव ! हमारी प्रार्थना को सुनकर आप यज्ञस्थल पर आयें। आपके निमित्त सोमरस प्रस्तुत है, इसका पान करें
- **Translation**: 

---

### Verse 10 (Rig Ved 0.30)
- **Original**: 11. वाय उक्थेभिर्जरन्ते त्वामच्छा जरितार:। -सुतसोमा अहर्विद:
- **Translation**: 

---

### Verse 11 (Rig Ved 0.31)
- **Original**: हे वायुदेव ! सोमरस तैयार करके रखने वाले, उसके गुणों को जानने वाले स्तोतागण स्तोत्रों से आपकी उत्तम प्रकार से स्तुति करते हैं
- **Translation**: 

---

### Verse 12 (Rig Ved 0.32)
- **Original**: 12. वायो तव प्रपृक्तती धेना जिगाति दाशुषे। उरूची सोमपीतये
- **Translation**: 

---

### Verse 13 (Rig Ved 0.33)
- **Original**: हे वायुदेव ! आपकी प्रभावोत्यादक वाणों, सोमयाग करने वाले सभी यजमानों की प्रशंसा करती हुई एवं सोमरस का विशेष गुण-गान करती हुई, सोमरस पान करने को अभिलाषा से दाता (यजमान ) के पास पहुँचती है
- **Translation**: 

---

### Verse 14 (Rig Ved 0.34)
- **Original**: 13. इन्द्रबायू इमे सुता उप प्रयोभिरा गतम्‌। इन्दवों वामुशन्ति हि
- **Translation**: 

---

### Verse 15 (Rig Ved 0.35)
- **Original**: हे इन्द्रदेव ! हे वायुदेव ! यह सोमरस आपके लिये अभिषुत किंया (निचोड़ा) गया है। आप अनादि पदार्थों के साथ यहाँ पधारें, क्योंकि यह सोमरस आप दोनों की कामना करता है
- **Translation**: 

---

### Verse 16 (Rig Ved 0.36)
- **Original**: 14 वायविन्धश्च चेतथ: सुतानां वाजिनीवसू। तावा यातमुप द्रवत्‌
- **Translation**: 

---

### Verse 17 (Rig Ved 0.37)
- **Original**: हे बायुदेव ! हे इद्धदेव ! आप दोनों अनादि पदार्थों और घन से परिपूर्ण हैं एवं अभिषुत सोमरस की विशेषता को जानते हैं। अत: आप दोनों शीघ्र ही इस वज्ञ में पदार्पण करें
- **Translation**: 

---

### Verse 18 (Rig Ved 0.38)
- **Original**: 15. वायविन्द्धश्न सुन्वत आ यातमुप निष्कृतम्‌। मश्षविशत्था धिया नरा
- **Translation**: 

---

### Verse 19 (Rig Ved 0.39)
- **Original**: है वायुदेव ! हे इन््रदेव ! आप दोनों बड़े सामर्थ्यशाली हैं। आप यजमान द्वाग़ बुद्धिपूर्वक निष्पादित सोम के पास अति शीघ्र पधघारें
- **Translation**: 

---

### Verse 20 (Rig Ved 0.40)
- **Original**: मं0 9 सू0 3 ढे 16. मित्र हुवे पूतदक्ष॑ बरुणं च रिशादसम्‌। धियं घृताचीं साधन्ता
- **Translation**: 

---

