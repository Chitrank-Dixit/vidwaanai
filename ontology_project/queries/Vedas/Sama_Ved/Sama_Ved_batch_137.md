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

### Verse 1 (Sama Ved 0.2721)
- **Original**: 1050.पवीतार: पुनीतन सोममिन्द्राय पातवे । अथा नो वस्यसस्कृधि
- **Translation**: 

---

### Verse 2 (Sama Ved 0.2722)
- **Original**: है सोमरस शोधित करने वाले याजको ! इन््रदेव के पान हेतु सोमरस को पवित्र करो । (जिसे पीकर) वे हमारा कल्याण करें
- **Translation**: 

---

### Verse 3 (Sama Ved 0.2723)
- **Original**: 1051.तवं सूर्येन आ भज तब क्रत्वा तवोतिभि:। अथा नो वस्यसस्कृधि
- **Translation**: 

---

### Verse 4 (Sama Ved 0.2724)
- **Original**: हे सोमदेव ! आप अपने सत्कर्मों और संरक्षण युक्त साधनों से हमें सूयोपासना की ओर प्रेरित करें, जिससे हमारा श्रेष्ठ हित हो
- **Translation**: 

---

### Verse 5 (Sama Ved 0.2725)
- **Original**: 1052.तव क्रत्वा तवोतिभिज्योक्पश्येम सूर्यम्‌ । अथा नो वस्यसस्कृधि
- **Translation**: 

---

### Verse 6 (Sama Ved 0.2726)
- **Original**: । हे सोमदेव ! आपके द्वारा प्रदत्त सदज्ञान से एवं आपके संरक्षण से युक्त हम बहुत वर्षों तक सूर्य दर्शन से लाभान्वित हों अर्थात्‌ दीर्घायुष्य प्राप्त करें और हमें कल्याण की प्राप्ति हो
- **Translation**: 

---

### Verse 7 (Sama Ved 0.2727)
- **Original**: 6 । । 1053.अभ्यर्ष स्वायुध सोम द्विबहस॑ रयिम्‌। अथा नो वस्यसस्कृधि
- **Translation**: 

---

### Verse 8 (Sama Ved 0.2728)
- **Original**: हे श्रेष्ठ शस््रधारी सोमदेव ! लौकिक और पारलौकिक दोनों प्रकार के धन से आप हमें सम्पन्न करें, जिससे हम सुख प्राप्त करें
- **Translation**: 

---

### Verse 9 (Sama Ved 0.2729)
- **Original**: 1054.अभ्य3र्षानपच्युतो वाजिन्त्समत्सु सासहि: । अथा नो वस्यसस्कृधि
- **Translation**: 

---

### Verse 10 (Sama Ved 0.2730)
- **Original**: हे शक्ति-सम्पन्न सोमदेव ! युद्धभूमि में विजयी होने वाले और बैरियों को पराजित करने वाले आप कलश में स्थापित हों और हमें कल्याण की प्राप्ति हो
- **Translation**: 

---

### Verse 11 (Sama Ved 0.2731)
- **Original**: 1055.त्वां यज्ैरवीवृधन्पवरमान विधर्मण । अथा नो वस्यसस्कृधि
- **Translation**: 

---

### Verse 12 (Sama Ved 0.2732)
- **Original**: हे पवित्रता से युक्त सोमदेव ! अति फलदायक यज्ञ में यजमान उत्तम स्तोत्रों का गान करते हुए आपकी महिमा को बढ़ाते हैं, इसलिए हमें आप कल्याण से युक्त बनाएँ
- **Translation**: 

---

### Verse 13 (Sama Ved 0.2733)
- **Original**: 1056.रथिं नश्चित्रमश्विनमिन्दो विश्वायुमा भर । अथा नो वस्यसस्कृधि
- **Translation**: 

---

### Verse 14 (Sama Ved 0.2734)
- **Original**: हे सोमदेव ! हमें विचित्र अश्वों से सम्पन्न और सर्वलोक-हितकारी वैभव पर्याप्त मात्रा में प्रदान करें, जिससे हम सुख को प्राप्त करें
- **Translation**: 

---

### Verse 15 (Sama Ved 0.2735)
- **Original**: 1057.तरत्स मन्दी धावति धारा सुतस्यान्धसः । तरत्स मन्दी धावति
- **Translation**: 

---

### Verse 16 (Sama Ved 0.2736)
- **Original**: हर्षदायक, उत्तम पोषक तत्त्वों से युक्त सोमरस धारा, शोधन यन्त्र द्वारा पवित्र होकर तीव वेग से प्रवाहित होती है । आनन्द से युक्त वह सोमरस शोधित स्थिति में प्रवाहित होता है
- **Translation**: 

---

### Verse 17 (Sama Ved 0.2737)
- **Original**: 1058.उस्नरा वेद वसूनां मर्तस्य देव्यवस: । तरत्स मन्दी धावति
- **Translation**: 

---

### Verse 18 (Sama Ved 0.2738)
- **Original**: सभी प्रकार के वैभव से युक्त, देदीप्यमान-धाराएँ याजक का हर प्रकार से संरक्षण करना जानती हैं; ऐसी आनन्द प्रदायक धाराएँ तेज गति से प्रवाहित होती हैं
- **Translation**: 

---

### Verse 19 (Sama Ved 0.2739)
- **Original**: 1059. ध्वस्नयो: पुरुषन्त्योरा सहस्नाणि दग्महे । तरत्स मन्दी धावति
- **Translation**: 

---

### Verse 20 (Sama Ved 0.2740)
- **Original**: डे सामवेद-संहिता ध्वस््र और पुरुषन्ति नामक दुष्ट प्रकृति के राजाओं के अपार वैभव को हम प्राप्त करें । ऐसा करने में समर्थ आननन्‍्दप्रद सोम अतिवेग से प्रवाहित हो रहा है
- **Translation**: 

---

