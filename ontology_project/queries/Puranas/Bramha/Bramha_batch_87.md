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

### Verse 1 (Bramha 0.1721)
- **Original**: द्रष्पकर्मगुणारस्भ: कालपुष्पफलप्रद:। आदिश्चान्तश्न मध्यश्ष गायत्र्योड्डार एबं च
- **Translation**: 

---

### Verse 2 (Bramha 0.1722)
- **Original**: हसितो लोहित: कृष्णो नीलः पोतस्तथारुण:। कद्दु्ं कपिलो बधु: कपोतों मेचकस्तथा
- **Translation**: 

---

### Verse 3 (Bramha 0.1723)
- **Original**: सुवर्णरेता विख्यात: सुवर्णश्राप्पयो मतः। सुवर्णामा च तथा सुवर्णप्रिय एवं च
- **Translation**: 

---

### Verse 4 (Bramha 0.1724)
- **Original**: त्वमिन्द्रश्व यमथैव वरुणो धनदो5निल:। उत्पुल्लश्षित्रभानुश्ष॒ स्वर्भानुर्भानरेव.. च
- **Translation**: 

---

### Verse 5 (Bramha 0.1725)
- **Original**: होत्र होता च होम्यं च हुतं चैत्र तथा प्रभु:। त्रिसौपर्णस्तथा ब्रह्मनू यजु्षां शतरुद्रियम्‌
- **Translation**: 

---

### Verse 6 (Bramha 0.1726)
- **Original**: पवित्र च पत्रित्राणां मड्न्‍नलानां च मड़ुलम्‌। प्राणश्र त्व॑ रजश्ल त्वं तम: सत्ययुतस्तथा
- **Translation**: 

---

### Verse 7 (Bramha 0.1727)
- **Original**: प्राणोईपान: समानश्ष उदानों व्यान एवं च। उन्मेषक्ष निमेषश्च क्षुतृद््‌ जुप्भा तथैंब च
- **Translation**: 

---

### Verse 8 (Bramha 0.1728)
- **Original**: लोहिताड्श्च दंट्टरी घ महावकक्‍्त्रोे महोदर:। शुचिरोपमा . हरिच्छपश्रुरूथ्वकेशधलाचल:
- **Translation**: 

---

### Verse 9 (Bramha 0.1729)
- **Original**: गीतवादित्रनृत्याब्रो गीतवादनकप्रिय:। मत्स्यो जालो जलो5जय्यो जलब्याल: कुटीचर:
- **Translation**: 

---

### Verse 10 (Bramha 0.1730)
- **Original**: विकालश्च॒ सुकालश्च॒ दुष्काल: कालनाशन:। मृत्युश्नैवाक्षयो5न्तश्ल क्षमा माया करोत्कर:
- **Translation**: 

---

### Verse 11 (Bramha 0.1731)
- **Original**: संवर्तोी. वर्तकक्बैव. संवर्तकबलाहकौ। घण्टाकी घण्टकी घण्टी चूडालो लवणोदधि:
- **Translation**: 

---

### Verse 12 (Bramha 0.1732)
- **Original**: + दक्षद्वारा भगवान्‌ शिवकी स्तुति * <7 तीनों लोकोंकी रक्षा आपके ही हाथोंमें है। , तृषा, चुढ़ापा, आधि (मानसिक पीड़ा) और गोविन्द (गोरक्षक), गोफपालक और गौओंके मार्ग
- **Translation**: 

---

### Verse 13 (Bramha 0.1733)
- **Original**: व्याधि भी आप ही हैं। व्याधिके नाशक और भी आप ही हैं। आपका मुख पूर्ण चन्द्रके समान
- **Translation**: 

---

### Verse 14 (Bramha 0.1734)
- **Original**: पालक भी आप ही हैं। आप सहन करने योग्य, आह्वादक है। आप सुन्दर मुखवाले हैं। जिनका
- **Translation**: 

---

### Verse 15 (Bramha 0.1735)
- **Original**: यज्ञरूपी मृगके मारनेवाले व्याध, व्याधियोंके आकर मुख सुन्दर नहीं है, जो मुखसे रहित हैं, जिनके
- **Translation**: 

---

### Verse 16 (Bramha 0.1736)
- **Original**: (भंडार) तथा अकर (कुछ भी न करनेवाले) चार या अनेक मुख हैं तथा जो सदा युद्धमें
- **Translation**: 

---

### Verse 17 (Bramha 0.1737)
- **Original**: हैं। आप शिखण्डी (मोरपंखधारी), पुण्डरीक सम्मुख डटे रहते हैं, जे सब भी आपके हो
- **Translation**: 

---

### Verse 18 (Bramha 0.1738)
- **Original**: (कमलरूप) तथा पुण्डरीकलोचन हैं । दण्डधृक्‌ ', स्वरूप हैं। आप हिरण्यगर्भ (ब्रह्मा), शकुनि
- **Translation**: 

---

### Verse 19 (Bramha 0.1739)
- **Original**: चक्रदण्ड* तथा रौद्रभागाविनाशनौ-- ये सब आपके (बाज), धनद (धन देनेबाले), धनके स्वामी,
- **Translation**: 

---

### Verse 20 (Bramha 0.1740)
- **Original**: ही नाम हैं।* आप विष, अमृत, देवपेय, दुग्ध, विय्द्‌, अधर्मका नाश करनेबाले, महादक्ष, दण्डधारी
- **Translation**: 

---

