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

### Verse 1 (Bramha 0.6181)
- **Original**: (191। 2-5)
- **Translation**: 

---

### Verse 2 (Bramha 0.6182)
- **Original**: * अक्वूरका नन्दगाँवमें जाना, श्रीयम-कृष्णकी मथुरा-यात्रा * 299 सिम यश कलट- --्सचच्च््क््िििंख़ेू)ू€ जि ओाओआाओओ््न्ओओओओओआआिओिनििईओओअओअथ़?ट्िशअओओे रुद्र, अश्विनीकुमार, बसु, आदित्य तथा मरुद्रण
- **Translation**: 

---

### Verse 3 (Bramha 0.6183)
- **Original**: करनेपर मनुष्य पूर्ण कल्याणका भागी होता है, जिनके स्वरूपको नहीं जानते, वे श्रीहरि आज
- **Translation**: 

---

### Verse 4 (Bramha 0.6184)
- **Original**: उन पुरुषश्रेष्ठ श्रीहरिकी मैं सदाके लिये शरण मेश स्पर्श करेंगे। जो सर्वात्मा, सर्वव्यापी, सर्वस्वरूप,
- **Translation**: 

---

### Verse 5 (Bramha 0.6185)
- **Original**: लेता हूँ।* सम्पूर्ण भूतोंमें स्थित, अव्यय एवं व्यापी परमात्मा
- **Translation**: 

---

### Verse 6 (Bramha 0.6186)
- **Original**: . अक्रूरका हृदय भक्तिसे विनप्न हो रहा था। वे हैं, ये ही आज मेरे नेत्रोंके अतिथि होंगे। जिन्होंने
- **Translation**: 

---

### Verse 7 (Bramha 0.6187)
- **Original**: इस प्रकार श्रीविष्णुका चिन्तन करते हुए कुछ अपनी योगशक्तिसे मत्स्य, कूर्म, बराह और
- **Translation**: 

---

### Verse 8 (Bramha 0.6188)
- **Original**: दिन रहते नन्दर्गाँवमें पहुँच गये। वहाँ उन्होंने नरसिंह आदि अवतार ग्रहण किये थे, वे ही
- **Translation**: 

---

### Verse 9 (Bramha 0.6189)
- **Original**: भगवान्‌ श्रीकृष्णको उस स्थानपर देखा, जहाँ गौएँ भगवान्‌ आज मुझसे वार्तालाप करेंगे। स्वेच्छासे
- **Translation**: 

---

### Verse 10 (Bramha 0.6190)
- **Original**: दुही जा रही थीं। वे बछड़ोंके बीचमें खड़े थे। शरीर धारण करनेवाले अविनाशी जगन्नाथ इस
- **Translation**: 

---

### Verse 11 (Bramha 0.6191)
- **Original**: उनका श्रीअड्भ विकसित नौलकमलकी आभासे समय कार्यवश ब्रजमें निवास करनेके लिये
- **Translation**: 

---

### Verse 12 (Bramha 0.6192)
- **Original**: सुशोभित था। नेत्र खिले हुए कमलकी शोभा मुझे ' अक्रूर' कहकर बुलायेंगे। पिता, पुत्र, सुददद,
- **Translation**: 

---

### Verse 13 (Bramha 0.6193)
- **Original**: मुसकानसे सुशोभित मुख, लाल-लाल नख, भ्राता, माता और बन्धु-बान्धवरूपिणी जिनकी
- **Translation**: 

---

### Verse 14 (Bramha 0.6194)
- **Original**: शरीरपर पीताम्बर, गलेमें जंगली पुष्पोंके हार, मायाको यह जगत्‌ हटा नहीं पाता, उन भगवान्‌को
- **Translation**: 

---

### Verse 15 (Bramha 0.6195)
- **Original**: हाथमें स्निग्ध नील लता और कानोंमें श्वेत बारंबार नमस्कार है। जिनको हृदयमें स्थापित
- **Translation**: 

---

### Verse 16 (Bramha 0.6196)
- **Original**: कमलपुष्पके आभूषण-यहीं उनकी झाँकी थी। करके मनुष्य इस योगमायारूप फैली हुई अविद्याको
- **Translation**: 

---

### Verse 17 (Bramha 0.6197)
- **Original**: उनके दोनों चरण भूमिपर विराजमान थे। श्रीकृष्णका तर जाते हैं, उन विद्यास्वरूप परमात्माकों नमस्कार
- **Translation**: 

---

### Verse 18 (Bramha 0.6198)
- **Original**: दर्शन करनेके बाद अक्रूरजीकी दृष्टि यदुनन्दन है। जिन्हें यज्ञपरायण मनुष्य यज्ञपुरुष, भगवद्धक्त-
- **Translation**: 

---

### Verse 19 (Bramha 0.6199)
- **Original**: बलभद्गजीपर पड़ी, जो हंस, चन्द्रमा और कुन्दके जन जासुदेव और वेदान्तवेत्ता सर्वव्यापी श्रीविष्णु
- **Translation**: 

---

### Verse 20 (Bramha 0.6200)
- **Original**: समान गौरवर्ण थे। उनके शरीरपर नील वस्त्र कहते हैं, उनको मेरा नमस्कार है। जो सम्पूर्ण
- **Translation**: 

---

