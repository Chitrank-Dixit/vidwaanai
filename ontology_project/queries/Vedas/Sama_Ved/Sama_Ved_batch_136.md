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

### Verse 1 (Sama Ved 0.2701)
- **Original**: 1049. समुद्रो अप्सु मामृजे विष्टम्भो धरुणो दिवः । सोम: पवित्रे अस्मयु:
- **Translation**: 

---

### Verse 2 (Sama Ved 0.2702)
- **Original**: जलयुक्त, देवलोक का धारक, आधारभूत, इच्छित सोम, पात्र के जल में बार-बार शोधित किया जाता है
- **Translation**: 

---

### Verse 3 (Sama Ved 0.2703)
- **Original**: 1042.अचिक्रददवृषा हरिर्महान्मित्रो न दर्शतः । सं सूर्येण दिद्युते
- **Translation**: 

---

### Verse 4 (Sama Ved 0.2704)
- **Original**: शक्तिवर्द्धक, हरितवर्ण, महानता युक्त तथा मित्र के समान दर्शन योग्य सोम, आवाज करते हुए सूर्यदेव की तरह प्रकाशित होता है
- **Translation**: 

---

### Verse 5 (Sama Ved 0.2705)
- **Original**: 1043.गिरस्त इन्द ओजसा मर्मुज्यन्ते अपस्युव:। याभिर्मदाय शुम्भसे
- **Translation**: 

---

### Verse 6 (Sama Ved 0.2706)
- **Original**: है सोमदेव ! आपकी शक्ति-सामर्थ्य से ही कर्म की प्रेरणा पाने वाले स्तोतागण वेदमन्त्रों का उच्चारण करते हैं और स्तुति-मन्त्रों द्वारा आनन्दवृद्धि के लिए आपको सुशोभित करते हैं
- **Translation**: 

---

### Verse 7 (Sama Ved 0.2707)
- **Original**: 1044.त॑ त्वा मदाय घृष्वय उ लोककूलुमीमहे । तब प्रशस्तये महे
- **Translation**: 

---

### Verse 8 (Sama Ved 0.2708)
- **Original**: संसार के कल्याण की इच्छा से शत्रुओं का संहार करने वाले हे सोमदेव ! महात्‌ स्तोत्रों से युक्त हम, आनन्दवृद्धि के लिए आपकी स्तुति करते हैं
- **Translation**: 

---

### Verse 9 (Sama Ved 0.2709)
- **Original**: 1045. गोषा इन्दो नृषा अस्यश्वसा वाजसा उत । आत्मा यज्ञस्य पूर्व्य:
- **Translation**: 

---

### Verse 10 (Sama Ved 0.2710)
- **Original**: है सोमदेव ! यज्ञ के मूल तथा प्रमुख आत्मा के रूप में आप गौ, अश्वु, अन्न और सुसन्तति प्रदान करने बाले हैं
- **Translation**: 

---

### Verse 11 (Sama Ved 0.2711)
- **Original**: [ वैदिक कालीन यज्ञों में सोप को अनिवार्य माता गया था। सोम न हो तो यज्ञ भी सम्भव नहीं, अतएव इसे यज्ञ की आत्पा कहा गया है ।] 1046. अस्मभ्यमिन्दविन्द्रियं मधो: पवस्व धारया । पर्जन्यो वृष्टिमाँ डूब
- **Translation**: 

---

### Verse 12 (Sama Ved 0.2712)
- **Original**: हे सोमदेव ! प्राण-पर्जन्य की वर्षा के समान हमारी इन्द्रियों की शक्ति-सामर्थ्य कों आप अपनी अमृत रूपी मधुर धारा से बढ़ाएँ
- **Translation**: 

---

### Verse 13 (Sama Ved 0.2713)
- **Original**: इति प्रथम: खण्ड:
- **Translation**: 

---

### Verse 14 (Sama Ved 0.2714)
- **Original**: द्वितीय: खण्ड:
- **Translation**: 

---

### Verse 15 (Sama Ved 0.2715)
- **Original**: । 1047.सना च सोम जैषि च पवमान महि श्रव: । अथा नो वस्यसस्कृधि
- **Translation**: 

---

### Verse 16 (Sama Ved 0.2716)
- **Original**: अतितस्तुत्य, पवित्र हे सोमदेव ! आप देवशक्तियों को उपलब्ध हों तथा शत्रुओं पर विजय प्राप्ति के बाद हमें कीर्तिमान्‌ बनाएँ
- **Translation**: 

---

### Verse 17 (Sama Ved 0.2717)
- **Original**: 1048.सना ज्योति: सना स्व3र्विश्वा च सोम सौभगा ।अथा नो वस्यसस्कृधि
- **Translation**: 

---

### Verse 18 (Sama Ved 0.2718)
- **Original**: उत्तराचिंके सप्तमो5 ध्यायः 73 हे सोम ! हमें तेजस्विता प्रदान करें । सभी स्वरगोंपम सुख और सौभाग्य देते हुए हमारा कल्याण करें
- **Translation**: 

---

### Verse 19 (Sama Ved 0.2719)
- **Original**: 1049.सना दक्षमुत क्रतुमप सोम मृथो जहि । अथा नो वस्यसस्कृधि
- **Translation**: 

---

### Verse 20 (Sama Ved 0.2720)
- **Original**: है सोमदेव ! आप हमें बल और यज्ञीय कर्ततव्य-शक्ति प्रदान करें, शत्रुपक्ष को पराजित करके आप हमारा कल्याण करें
- **Translation**: 

---

