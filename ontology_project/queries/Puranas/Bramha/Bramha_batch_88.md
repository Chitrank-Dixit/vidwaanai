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

### Verse 1 (Bramha 0.1741)
- **Original**: सोम, मधु, जल तथा सब कुछ पान करनेवाले हैं। तथा युद्धके प्रेमी हैं। खड़े रहनेवाले, स्थिर, [चल और अबल सब आप ही हैं। स्थाणु, निष्कम्प, अत्यन्त निश्चल, दुर्वारण (कठिनतासे
- **Translation**: 

---

### Verse 2 (Bramha 0.1742)
- **Original**: आप धर्ममय वृषभके शरीरपर सवार होने निवारण किये जाने योग्य), दुर्विषह (असहा),
- **Translation**: 

---

### Verse 3 (Bramha 0.1743)
- **Original**: योग्य हैं, बृषभस्वरूप हैं। आपके नेत्र वृषभके दुस्सह और दुरतिक्रम (दुर्लदध्य) हैं। आपको
- **Translation**: 

---

### Verse 4 (Bramha 0.1744)
- **Original**: नेत्रोंके समान हैं। आप वृषभके नामसे लोकपें धारण करना या वशमें लाना कठिन है। आप
- **Translation**: 

---

### Verse 5 (Bramha 0.1745)
- **Original**: विख्यात हैं। सम्पूर्ण लोक आपका संस्कार (पूजन नित्य दुर्दम्य (कठिनतासे दमन करने योग्य),
- **Translation**: 

---

### Verse 6 (Bramha 0.1746)
- **Original**: और अभिषेक) करता है। शिव! चन्द्रमा और विजय एवं जय हैं। आप शश (खरगोश)-रूप
- **Translation**: 

---

### Verse 7 (Bramha 0.1747)
- **Original**: सूर्य आपके नेत्र, ब्रह्माजी हृदय, अग्रिप्टोम शरीर हैं। चन्द्रमा आपके नेत्र हैं। आप एक ही साथ
- **Translation**: 

---

### Verse 8 (Bramha 0.1748)
- **Original**: और धर्मकर्म भृज्जार हैं। ब्रह्मा, विष्णु तथा प्राचीन शीत और उष्ण दोनों ही धारण करते हैं। क्षुधा,
- **Translation**: 

---

### Verse 9 (Bramha 0.1749)
- **Original**: ऋषि भी आपके माहात्म्यकों यथार्थरूपसे जाननेमें 3. दण्डधारी, 2. चक्रद्धाए दण्ड देनेवाले, 3. रूरके भागका नाश न होने देनेबाले। भगनेत्रान्तकक्षण्ड:. पृष्णो.. दन्तविनाशन:। स्वाहा स्वधा बषद्कारों। नमस्कार नमोस्तु ते
- **Translation**: 

---

### Verse 10 (Bramha 0.1750)
- **Original**: गृूहव्तक्ष गूढक्ष गूढब्रतनिषेवित:। तरणस्तारणबैव सर्वभूतेषु ताएण:
- **Translation**: 

---

### Verse 11 (Bramha 0.1751)
- **Original**: धाता विधाता संधाता निधाता धारणो धर:। तपो ब्रह्म च सत्य॑ च ब्रह्मचर्य॑ तथा55र्जबम्‌
- **Translation**: 

---

### Verse 12 (Bramha 0.1752)
- **Original**: भूतात्मा. भूतकृएभूतों. भूतभव्यभवोद्धव:। भूर्भुव:ः स्वरितश्षेव भूतो हा्रिमहेंश्वर:
- **Translation**: 

---

### Verse 13 (Bramha 0.1753)
- **Original**: ब्रह्मावर्त: सुराबर्त: कामावर्त नमोस्तु ते। कामबिम्बविनिर्हन्ता कर्णिकारस्नजप्रिय:
- **Translation**: 

---

### Verse 14 (Bramha 0.1754)
- **Original**: गोनेता. गोप्रचारक्ष गोवृषे श्वृर्याहन:। ्ैलोक्यगोसा गोबिन्दो गोप्ता गोमार्ग एवं च
- **Translation**: 

---

### Verse 15 (Bramha 0.1755)
- **Original**: अछण्डचन्द्राभिमुख: सुमुखों दुर्मुखओोःमुख:। चतुर्मुखो बहुपुखो रणेप्वभियुख: सदा
- **Translation**: 

---

### Verse 16 (Bramha 0.1756)
- **Original**: हिरण्यगर्भ : शकुनिर्धनदो3र्थपतिविराट्‌ । अधर्महा महादक्षो दण्डधारों रणप्रिय:
- **Translation**: 

---

### Verse 17 (Bramha 0.1757)
- **Original**: तिए्ठन्‌ स्थिरक्ष स्थाणुश्च निष्कम्पक्ष सुनिश्चल:। दुर्वारणो दुर्विषहों दुःसहो दुरतिक्रम:
- **Translation**: 

---

### Verse 18 (Bramha 0.1758)
- **Original**: दुर्धरो दुर्वशों नित्यो दुर्दपों बिजयो जय:। शश: शशाडुतयत्र: शीतरोष्ण: क्षुतृपषा जरा
- **Translation**: 

---

### Verse 19 (Bramha 0.1759)
- **Original**: आ आधवो व्याधयक्षैव व्याधिहा व्याधिपशक्च य:। सह्यो यज्ञमृगव्याधो व्याधीनामाकरों 5करः
- **Translation**: 

---

### Verse 20 (Bramha 0.1760)
- **Original**: शिखण्डी पुण्डरोकक्ष॒ पुण्डरीकावलोकन:। दण्डधूकू. चक्रदण्डक्ष रौद्रभागाविनाशन: #
- **Translation**: 

---

