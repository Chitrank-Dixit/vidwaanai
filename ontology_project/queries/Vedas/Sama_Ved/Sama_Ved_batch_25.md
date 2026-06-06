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

### Verse 1 (Sama Ved 0.481)
- **Original**: 168, अभि प्र गोपति गिरेन्द्रमर्च यथा विदे। सूनुं सत्यस्थ सत्पतिम्‌
- **Translation**: 

---

### Verse 2 (Sama Ved 0.482)
- **Original**: है याजको ! गौ पालक, सत्यनिष्ठ सज्जनों के संरक्षक इद्धदेव को मन्नोच्चारण सहित प्रार्थना करो, जिससे उनकी शक्तियों का आभास हो
- **Translation**: 

---

### Verse 3 (Sama Ved 0.483)
- **Original**: 169, कया नश्वित्र आ भुवदूती सदावृध: सखा । कया शचिष्ठया बृता
- **Translation**: 

---

### Verse 4 (Sama Ved 0.484)
- **Original**: निरन्तर प्रगतिशील इनद्धदेव ! आप किन-किन तृप्तिकारक पदार्थों के भेंट करने से, किस तरह की पूजा-विधि से प्रसन्न होकर, आप किन दिव्यशक्तियों सहित हमारे सहयोगी बनेंगे ?
- **Translation**: 

---

### Verse 5 (Sama Ved 0.485)
- **Original**: 170. त्यमु वः सत्रासाहं विश्वासु गीरष्वायतम्‌ । आ च्यावयस्यूतये'
- **Translation**: 

---

### Verse 6 (Sama Ved 0.486)
- **Original**: है याजको ! अपनी सप्रस्त वाणियों में वर्णित स्तृतियों से, अपने संरक्षण के लिए, असुरजयी इन्द्रदेव का आवाहन करो
- **Translation**: 

---

### Verse 7 (Sama Ved 0.487)
- **Original**: पूर्वार्चिकि ऐजडपर्वणि ह्वितीयो उध्याय: 2.7 171. सदसस्पतिमद्भुतं प्रियमिन्द्रस्य काम्यम्‌। सनिं मेधामयासिषम्‌
- **Translation**: 

---

### Verse 8 (Sama Ved 0.488)
- **Original**: इन्द्रदेव को प्रिय, काम्य पदार्थों को देने में समर्थ, लोकों का मर्म समझने में सक्षम, अद्भुत मेधा को हमने प्राप्त किया
- **Translation**: 

---

### Verse 9 (Sama Ved 0.489)
- **Original**: 172. ये ते पनथा अधो दिबो येभिव््यश्वमैरय: । उत ओ्रोषन्तु नो भुव:
- **Translation**: 

---

### Verse 10 (Sama Ved 0.490)
- **Original**: हे इन्रदेव ! चुलोक से पृथ्वी की ओर उन्मुख आपके मार्ग, जिनसे आप सृष्टि का संचालन करते हैं, वे (मार्ग) हमारे यज्ञ स्थल तक पहुँचते हैं, उन्हीं मार्गों से आप हमारे यज्ञ स्थान में पहुँचें
- **Translation**: 

---

### Verse 11 (Sama Ved 0.491)
- **Original**: 173. भद्वंभद्वं न आ भरेषमूर्ज शतक़तो । यदिन्द्र मृडयासि न:
- **Translation**: 

---

### Verse 12 (Sama Ved 0.492)
- **Original**: है शतक्रतु इद्धदेव ! सुखकारी, अल-बल से युक्त ऐश्वर्य आप हमें भरपूर मात्रा में प्रदान करें, क्योंकि आप ही हमें सुखी बनाते हैं
- **Translation**: 

---

### Verse 13 (Sama Ved 0.493)
- **Original**: 174. अस्ति सोमो अयं॑ सुतः पिबन्त्यस्थ मरूत:। उत स्व॒राजों अश्विना
- **Translation**: 

---

### Verse 14 (Sama Ved 0.494)
- **Original**: हमारे द्वारा शोधित इस सोमरस का पान, तेजस्वी मरुद्गण तथा अश्विनीकुमार करते हैं
- **Translation**: 

---

### Verse 15 (Sama Ved 0.495)
- **Original**: इति षष्ठ: खण्ड:
- **Translation**: 

---

### Verse 16 (Sama Ved 0.496)
- **Original**: के के के
- **Translation**: 

---

### Verse 17 (Sama Ved 0.497)
- **Original**: सप्तम: खण्ड:
- **Translation**: 

---

### Verse 18 (Sama Ved 0.498)
- **Original**: 175. ईब्डुयन्तीरपस्युव इन्द्र जातमुपासते । वन्वानास: सुवीर्यम्‌
- **Translation**: 

---

### Verse 19 (Sama Ved 0.499)
- **Original**: उत्तम बल तथा कार्य की कामना वाली इन्द्रदेव की माता, प्रकट हुए इन्द्रदेव को सेवा करती हैं 1
- **Translation**: 

---

### Verse 20 (Sama Ved 0.500)
- **Original**: 176. न कि देवा इनीमसि न क्या योपयामसि । मन्त्रश्नुत्यं चरामसि
- **Translation**: 

---

