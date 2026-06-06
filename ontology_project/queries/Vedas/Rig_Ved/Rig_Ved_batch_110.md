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

### Verse 1 (Rig Ved 0.2181)
- **Original**: है सोमदेव ! हविदाता के सुखद जोवन के लिए अपने रक्षण-प्ामथ्यों से उसकी रक्षा करें
- **Translation**: 

---

### Verse 2 (Rig Ved 0.2182)
- **Original**: 997 इमं यज्ञमिदं वचो जुजुषाण उपागहि। सोम त्व॑ं नो वृथे भव
- **Translation**: 

---

### Verse 3 (Rig Ved 0.2183)
- **Original**: हे सोमदेव ! आप इस यज्ञ में हमारी इन स्तुतियों को स्वीकार करें । हमारे पास आयें और हमारी वृद्धि करें
- **Translation**: 

---

### Verse 4 (Rig Ved 0.2184)
- **Original**: 998. सोम गीर्भिष्टवा वय॑ वर्धवामो वचोविद:
- **Translation**: 

---

### Verse 5 (Rig Ved 0.2185)
- **Original**: सुमृव्दीको न आ विश
- **Translation**: 

---

### Verse 6 (Rig Ved 0.2186)
- **Original**: स्तुति वननों के ज्ञाता हे सोमदेव ! हम अपनी वाणियों से आपको बढ़ाते हैं । आप हमारे बीच सुख-साधनों को लेकर प्रविष्ट हों
- **Translation**: 

---

### Verse 7 (Rig Ved 0.2187)
- **Original**: 999. गयस्फानो अमीवहा वसुवित्पुष्टिवर्धन:
- **Translation**: 

---

### Verse 8 (Rig Ved 0.2188)
- **Original**: सुमित्र: सोम नो भव
- **Translation**: 

---

### Verse 9 (Rig Ved 0.2189)
- **Original**: है सोमदेव ! आप हमारी वृद्धि करने वाले,रोगों का नाश करते बाले, धन देने वाले, पुष्टि वर्धक और उत्तम पित्र बनें
- **Translation**: 

---

### Verse 10 (Rig Ved 0.2190)
- **Original**: 1000, सोम रारन्धि नो हृदि गावो न यवसेष्वा। मर्य इब स्व ओक्ये
- **Translation**: 

---

### Verse 11 (Rig Ved 0.2191)
- **Original**: हे सोमदेव ! गौएँ जैसे जौ के खेत में और मनुष्य जैसे अपने घर में रमण करता है, बैसे आप हमारे हृदय में रमण करें
- **Translation**: 

---

### Verse 12 (Rig Ved 0.2192)
- **Original**: 128 ऋग्वेद संहिता भाग-1 1001. यः सोम सख्ये तब रारणद्वेव मर्त्य:। त॑ दक्षः सचते कवि:
- **Translation**: 

---

### Verse 13 (Rig Ved 0.2193)
- **Original**: है सोमदेव ! जो याज़क आपकी मित्रता से युक्त रहता है,वही मेधावी और कुशल ज्ञानी हो जाता है
- **Translation**: 

---

### Verse 14 (Rig Ved 0.2194)
- **Original**: 1002. उरुष्या णो अभिशस्तेः सोम नि पाह्मांईस:। सखा सुशेव एधि न:
- **Translation**: 

---

### Verse 15 (Rig Ved 0.2195)
- **Original**: ह हे सोमदेव ! हमें अपयश से बचायें.। पाणों से हमें रक्षित करें औऔर हमारे निमित्त सुखकारी मित्र बनें
- **Translation**: 

---

### Verse 16 (Rig Ved 0.2196)
- **Original**: 1003. आ प्यायस्व समेतु ते विश्वत: सोम वृष्ण्यम्‌ू। भवा वाजस्थ सड़थे
- **Translation**: 

---

### Verse 17 (Rig Ved 0.2197)
- **Original**: है सोमदेव ! आप वृर्द्धि को प्राप्त हों । आप सभो ओर से बलों से युक्त हों । संग्राम में आप हमारे सहायक रूप हों
- **Translation**: 

---

### Verse 18 (Rig Ved 0.2198)
- **Original**: 1004. आ प्यायस्व मदिन्तम सोम विश्वेशिरंशुभि: । भवा न: सुश्रवस्तम: सखा वृधे
- **Translation**: 

---

### Verse 19 (Rig Ved 0.2199)
- **Original**: है अति आह्वादक सोमदेव ! अपने दिव्य गुणों की यश गाथाओं से चतुर्दिक्‌ विस्तार को प्राप्त करें । हमारे विकास के निमित्त मित्र रूप में आप सहयोग करें
- **Translation**: 

---

### Verse 20 (Rig Ved 0.2200)
- **Original**: 1005. सं ते पयांसि समु यन्तु वाजा: सं वृष्ण्यान्यभिमातिषाह: । आप्यायमानो अमृताय सोम दिवि श्रवांस्युत्तमानि धिष्व
- **Translation**: 

---

