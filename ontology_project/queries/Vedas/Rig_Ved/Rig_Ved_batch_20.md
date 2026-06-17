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

### Verse 1 (Rig Ved 0.381)
- **Original**: हे इन्द्र और वरुणदेवो ! हमारी कापनाओं के अनुरूप धन देकर हमें संतुष्ट करें
- **Translation**: 

---

### Verse 2 (Rig Ved 0.382)
- **Original**: आप दोनों के समीप पहुँचकर हम प्रार्थना करते हैं
- **Translation**: 

---

### Verse 3 (Rig Ved 0.383)
- **Original**: 171. युवाकु हि शचीनां युवाकु सुमतीनाम्‌। भूयाम वाजदान्वाम्‌
- **Translation**: 

---

### Verse 4 (Rig Ved 0.384)
- **Original**: हमारे कर्म संगठित हों, हमारी सदबुद्धियाँ संगठित हों, हम अग्रगण्य होकर दान करने वाले बनें
- **Translation**: 

---

### Verse 5 (Rig Ved 0.385)
- **Original**: 172, इन्द्रःसहस्रदाव्मां वरुण: शंस्यानाम्‌
- **Translation**: 

---

### Verse 6 (Rig Ved 0.386)
- **Original**: क्रतुर्भवत्युक्थ्य:
- **Translation**: 

---

### Verse 7 (Rig Ved 0.387)
- **Original**: इन्द्रदेव सहस्रों दाताओं में सर्वश्रेष्ठ हैं और वरुणदेव सहसरों प्रशंसनीय देवों में सर्वश्रेष्ठ हैं
- **Translation**: 

---

### Verse 8 (Rig Ved 0.388)
- **Original**: 20 ऋण्केद संहिता धाग-£ 173. तयोरिदवसा बय॑ सनेम नि च धीमहि। स्थादुत प्ररेचनम्‌
- **Translation**: 

---

### Verse 9 (Rig Ved 0.389)
- **Original**: आपके द्वारा सुरक्षित धन को प्राप्त कर हम उसका श्रेष्ठतम उपयोग करें । वह धन हमें बिपुल मात्रा में प्राप्त हो
- **Translation**: 

---

### Verse 10 (Rig Ved 0.390)
- **Original**: 174. इन्द्रावरुण वामहं हुवे चित्राय राधसे। अस्मान्त्सु जिग्युषस्कृतम्‌
- **Translation**: 

---

### Verse 11 (Rig Ved 0.391)
- **Original**: हे इन्द्रावरुण देवो ! विविध प्रकार के धन की कामना से हम आपका आवाहन करते हैं । आप हमें उत्तम विजय प्राप्त कराएँ
- **Translation**: 

---

### Verse 12 (Rig Ved 0.392)
- **Original**: 175, इन्द्रावरुण नू नु वां सिषासन्तीषु थीष्या। अस्मभ्यं शर्म बच्छतम्‌
- **Translation**: 

---

### Verse 13 (Rig Ved 0.393)
- **Original**: हे इन्द्रावरुण देवो ! हमारी बुद्धियाँ सम्यक्‌ रूप से आपकी सेवा करने की इच्छा करती हैं, अत: हमें शीघ्र ही निश्चयपूर्वक सुख प्रदान करें
- **Translation**: 

---

### Verse 14 (Rig Ved 0.394)
- **Original**: 176. प्र वामश्नोतु सुष्ठुतिरिन्द्रावरुण यां हुवे । यामृधाथे सथस्तुतिम्‌
- **Translation**: 

---

### Verse 15 (Rig Ved 0.395)
- **Original**: हे इद्रावरुण देवो ! जिन उत्तम स्तुतियों के लिए (प्रत्ति) हम, आप दोनों का आवाहन करते हैं एवं जिन स्तुतियों को साथ-साथ प्राप्त करके आप दोनों पुष्ट होते है, वे स्तुतियाँ आपको प्राप्त हों
- **Translation**: 

---

### Verse 16 (Rig Ved 0.396)
- **Original**: [ सूक्त - 18 ] [ऋषि- मेधातिथि काण्य । देवता- 1 - 3 ब्रह्मणस्पति, 4 इन्द्र, ब्रह्मणस्पति, सोम 5 ब्रह्मणस्पति, दक्षिणा, 6-8 सदसस्पति, 9 सदसस्पति या नराशंस । छन्द -गायत्री ।] 177 सोमान स्वरणं कृणुहि ब्रह्मणस्पते । कक्षीवन्तं य औशिज:
- **Translation**: 

---

### Verse 17 (Rig Ved 0.397)
- **Original**: हे सम्पूर्ण ज्ञान के अधिपति ब्रह्मणस्पति देव ! सोप का सेवन करने वाले यजमान को आप उशिज्‌ के पुत्र कक्षीवान्‌ की तरह श्रेष्ठ प्रकाश से युक्त करें
- **Translation**: 

---

### Verse 18 (Rig Ved 0.398)
- **Original**: 178. यो रेवान्‌ यो अमीवहा वसुवित्‌ पुष्टिवर्धन:। स न: सिषक्तु यस्तुरः
- **Translation**: 

---

### Verse 19 (Rig Ved 0.399)
- **Original**: ऐश्वर्यवान्‌, रोगों का नाश करने वाले, धन श्रदाता और पुष्टिवर्धक तथा जो शीघ्र फलदायक हैं, वे ब्रह्मणस्पतिदेव , हम पर कृपा करें
- **Translation**: 

---

### Verse 20 (Rig Ved 0.400)
- **Original**: 179. मा नः शंसो अररुषो धूर्ति: प्रणड्‌ मर्त्यस्य । रक्षा णो ब्रह्मणस्पते
- **Translation**: 

---

