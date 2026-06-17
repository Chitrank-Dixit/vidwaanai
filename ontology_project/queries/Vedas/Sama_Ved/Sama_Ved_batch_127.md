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

### Verse 1 (Sama Ved 0.2521)
- **Original**: 966,पवस्व वृत्रहन्तम उक्थेभिरनुमाद्यः । शुचि: पावकों अदभुत:
- **Translation**: 

---

### Verse 2 (Sama Ved 0.2522)
- **Original**: आश्चर्यजनक रीति से शत्रुओं का विनाश करने वाले, श्रेष्ठ वचनों द्वारा वन्दना करने योग्य हे सोमदेव ! आप शुद्धता और पवित्रता को प्राप्त करें
- **Translation**: 

---

### Verse 3 (Sama Ved 0.2523)
- **Original**: 967.शुचिः पावक उच्यते सोम: सुतः स मधुमान्‌। देवावीरघशंसहा
- **Translation**: 

---

### Verse 4 (Sama Ved 0.2524)
- **Original**: विधिपूर्वक तैयार किया गया, शुद्ध, संस्कारित और मधुर सोमरस, देवताओं ओ तृप्ति देने याला एवं दुष्टो का विनाश करने वाला (विकारों का शमन करने वाला) कहा गया है
- **Translation**: 

---

### Verse 5 (Sama Ved 0.2525)
- **Original**: इति प्रथम: खण्ड:
- **Translation**: 

---

### Verse 6 (Sama Ved 0.2526)
- **Original**: द्वितीय: खण्ड:
- **Translation**: 

---

### Verse 7 (Sama Ved 0.2527)
- **Original**: 968.,प्र कविर्देववीतये5व्या वारेभिरव्यत । साह्वान्विश्वा अभि स्पृध:
- **Translation**: 

---

### Verse 8 (Sama Ved 0.2528)
- **Original**: देवताओं को प्रदान करने के लिए यह ज्ञानवर्द्धक सोम उत्तम रीति से संस्कारित किया जाता है ! विकारनाशक यह सोम सभी शत्रुओं को परास्त करता है
- **Translation**: 

---

### Verse 9 (Sama Ved 0.2529)
- **Original**: 969.स हि ष्मा जरितृभ्य आ वाजं गोमन्तमिन्वति । पवमान: सहस्निणम्‌
- **Translation**: 

---

### Verse 10 (Sama Ved 0.2530)
- **Original**: पवित्रता को प्राप्त होने याले दिव्य सोम, स्तुति करने बाले याजकों को धन-धान्य प्रदान करके हर प्रकार से संतुष्ट करते हैं
- **Translation**: 

---

### Verse 11 (Sama Ved 0.2531)
- **Original**: 970.परि विश्वानि चेतसा मृज्यसे पवसे मती । स नः सोम श्रवों विद:
- **Translation**: 

---

### Verse 12 (Sama Ved 0.2532)
- **Original**: हे संस्कारित हुए वन्दनीय सोम ! आप हमें विचारपूर्वक अन्न के भण्डार प्रदान करें
- **Translation**: 

---

### Verse 13 (Sama Ved 0.2533)
- **Original**: 9791.अभ्यर्ष बृहद्यगों मघवद्धद्यो धुवं रयिम्‌। इषं स्तोतृभ्य आ भर
- **Translation**: 

---

### Verse 14 (Sama Ved 0.2534)
- **Original**: हे दिव्य सोम ! स्तुति करने वाले धनवान्‌ साधकों के लिए भी आप महान्‌ यश, स्थायी निधि एवं अन्न के भंडार प्रदान करें
- **Translation**: 

---

### Verse 15 (Sama Ved 0.2535)
- **Original**: उत्तराधिके वष्ठो5ध्याय: 6.3 972.त्वं राजेव सुद्रतो गिर: सोमा विवेशिध । पुनानो वल्ले अद्भुत
- **Translation**: 

---

### Verse 16 (Sama Ved 0.2536)
- **Original**: सत्कर्म में निरत, सद्भावना सम्पन्न, पवित्र हृदय वाले, स्वामी के समान हे दिव्य सोम ! याजकों द्वारा प्रस्तुत श्रेष्ठ वचनों (स्तुतियों) को आप स्वीकार करें
- **Translation**: 

---

### Verse 17 (Sama Ved 0.2537)
- **Original**: 973.स वह्ििरप्सु दुष्टरो मृज्यमानो ग्स्त्यो:
- **Translation**: 

---

### Verse 18 (Sama Ved 0.2538)
- **Original**: सोमश्चमूषु सीदति
- **Translation**: 

---

### Verse 19 (Sama Ved 0.2539)
- **Original**: यज्ञ सम्पन कराने वाला, हथेलियों की सहायता से शुद्ध किया जाता हुआ, जल मिश्रित सोम, पात्र में स्थिर होता है
- **Translation**: 

---

### Verse 20 (Sama Ved 0.2540)
- **Original**: 974.क्रीडुर्मखो न मंहयु: पवित्र॑ सोम गच्छसि । दथत्स्तोत्रे सुवीर्यम्‌
- **Translation**: 

---

