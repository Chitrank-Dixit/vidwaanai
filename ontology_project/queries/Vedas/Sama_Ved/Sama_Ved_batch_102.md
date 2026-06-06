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

### Verse 1 (Sama Ved 0.2021)
- **Original**: 778.पवस्वेन्दो बृषा सुतः कृधी नो यशसो जने । विश्वा अप द्विषो जहि
- **Translation**: 

---

### Verse 2 (Sama Ved 0.2022)
- **Original**: बलवर्द्धक, शोधिट किये गये हे सोमदेव ! पवित्र होकर आप हमें यशस्वी बनाएँ । हमारे शत्रुओं को आप पराजित करें
- **Translation**: 

---

### Verse 3 (Sama Ved 0.2023)
- **Original**: 779.यस्य ते सख्ये वयं सासह्याम पृतन्यतः । तवेन्दो द्युम्न उत्तमो
- **Translation**: 

---

### Verse 4 (Sama Ved 0.2024)
- **Original**: हे सोमदेव ! मित्र-भाव से आपने हमें तेजस्वी बनाया है, अः"/आपकी कृपा से) आक्रमणकारी शत्रुओं से हम विजय प्राप्त कर सकते हैं
- **Translation**: 

---

### Verse 5 (Sama Ved 0.2025)
- **Original**: 780.या ते भीमान्यायुधा तिग्मानि सन्ति धूर्वणे
- **Translation**: 

---

### Verse 6 (Sama Ved 0.2026)
- **Original**: रक्षा समस्य नो निद:
- **Translation**: 

---

### Verse 7 (Sama Ved 0.2027)
- **Original**: है सोमदेव ! शत्रुओं का नाश करने वाले अपने तौद्ष्ण शख्रों के द्वारा शत्रुओं की निन्‍दा से आहत होने से आप हमें बचाएँ
- **Translation**: 

---

### Verse 8 (Sama Ved 0.2028)
- **Original**: 781.वृषा सोम द्युमाँ असि वृषा देव वृषद्रतः । वृषा धर्माणि दक्चिषे
- **Translation**: 

---

### Verse 9 (Sama Ved 0.2029)
- **Original**: है सोमटेव ! आप तेजस्वी और बलशाली हैं । है स्वामी ! आप कामनाओं कौ पूर्ति करने वाले हैं, बलवर्द्धक हैं, ऐसे बती आप अपनी क्षमता से आचरण योग्य धर्मों के धारणकर्त्ता हैं
- **Translation**: 

---

### Verse 10 (Sama Ved 0.2030)
- **Original**: 782.वृष्णस्ते वृष्ण्यं शवो वृषा बन॑ वृषा सुतः । स्‌ त्व॑ वृषन्वृषेद्सि
- **Translation**: 

---

### Verse 11 (Sama Ved 0.2031)
- **Original**: है बलशाली सोमदेव ! आपकी बहुत ही प्रभावशाली सामर्थ्य है ! भापका पान करने वाले साधक, निश्चित रूप से उत्तम बल एवं'उत्तम सामर्थ्य से युक्त होते हैं
- **Translation**: 

---

### Verse 12 (Sama Ved 0.2032)
- **Original**: 3.2 सामवेद-संहिता 783.अश्वों न चक्रदो वृषा सं गा इन्दों समर्वतः। बिनो राये दुरों वृधि
- **Translation**: 

---

### Verse 13 (Sama Ved 0.2033)
- **Original**: है सोमदेव ! आप बलशालो हैं, पशुधन की वृद्धि करने वाले हैं। अत: आप हमें धर्म-मार्ग से ऐश्वर्य दिलाएँ
- **Translation**: 

---

### Verse 14 (Sama Ved 0.2034)
- **Original**: 784.वृषा हासि भानुना दुमन्तं त्वा हवामहे । पवमान स्वर्दशम्‌
- **Translation**: 

---

### Verse 15 (Sama Ved 0.2035)
- **Original**: है सोमदेव ! आप निश्चित ही बलवर्द्धक हैं । सुख के द्रष्टा, सूर्य जैसे दीप्तिमान्‌ , हे शोधित सोमदेव ! हम आपका आवाहन करते हैं
- **Translation**: 

---

### Verse 16 (Sama Ved 0.2036)
- **Original**: 785.यददिभ: परिषिच्यसे मर्मुज्यमान आयुभि: । द्रोणे सघस्थमश्नुषे
- **Translation**: 

---

### Verse 17 (Sama Ved 0.2037)
- **Original**: अ्रत्विजों द्रारा शोधित हे सोमदेव ! जल में मिलाये जाने के बाद आपको कलश में स्थापित किया जाता है
- **Translation**: 

---

### Verse 18 (Sama Ved 0.2038)
- **Original**: 786.आ पवस्व सुवीर्य॑ मन्दमान: स्वायुध
- **Translation**: 

---

### Verse 19 (Sama Ved 0.2039)
- **Original**: इहो ष्विन्दवा गहि
- **Translation**: 

---

### Verse 20 (Sama Ved 0.2040)
- **Original**: हे उत्तम आयुधों से युक्त सोम ! आनन्ददायी बनकर हमें श्रेष्ठ पराक्रम की क्षमता से युवत करें और हमारे यज्ञ में आकर सुशोभित हों
- **Translation**: 

---

