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

### Verse 1 (Markende Puran 0.2101)
- **Original**: गएर्कण्डेय उकान
- **Translation**: 

---

### Verse 2 (Markende Puran 0.2102)
- **Original**: 30 6 ततस्ती संहिता थिए्र तं॑ मुनि सपुपस्थिती
- **Translation**: 

---

### Verse 3 (Markende Puran 0.2103)
- **Original**: समाधिनाम चैश्योउसौ स च पार्थ्रिबप्त्तम:
- **Translation**: 

---

### Verse 4 (Markende Puran 0.2104)
- **Original**: कृत्वा तु तौ यथान्यायं यथाई तेब संविदम्‌
- **Translation**: 

---

### Verse 5 (Markende Puran 0.2105)
- **Original**: उपविष्टी कथाः ऋ्काश्रिच्चक्रतुर्वेश्यपार्थितों
- **Translation**: 

---

### Verse 6 (Markende Puran 0.2106)
- **Original**: 'प्रार्कण्डेचजी कहते हैं--
- **Translation**: 

---

### Verse 7 (Markende Puran 0.2107)
- **Original**: बअहान्‌! तदनन्तर राजाओंमें श्रेष्ठ सुरथ और चह सपाधि नामक वैश्य दोनों साथ-साथ भमेभ्रा मुनिको सेवामें उपस्थित हुए और उत्के साथ ब्रयायोग्व स्थाथनुकूल विनटपूर्ण जर्तांव करके सेठ; तत्पश्तात्‌ शैश्य और राजाने कुछ ब्रातलाप आग्म्ध किया
- **Translation**: 

---

### Verse 8 (Markende Puran 0.2108)
- **Original**: 1. पौ2-निष्कृतत: । 2, शा0--एस्फेनेत॑3 । राजोदाच / 19
- **Translation**: 

---

### Verse 9 (Markende Puran 0.2109)
- **Original**: भगर्य॑स्वामह प्रट्भिच्छाम्येक वदस्व ततू।
- **Translation**: 

---

### Verse 10 (Markende Puran 0.2110)
- **Original**: । दुःखाय यन्मे मनसः स्वत्तित्तायत्ञतां विना। ममत्व॑ गतरास्थस्थ 'राज्याड्रेज्चस्विलेष्यपि
- **Translation**: 

---

### Verse 11 (Markende Puran 0.2111)
- **Original**: जानक्ोषपषि यथाज्ञस्थ किमेतन्मुनिसत्तम्ा अर्य च निकृत: * पुवैदारेभभरुत्यैस्तथोज्ड्रितः
- **Translation**: 

---

### Verse 12 (Markende Puran 0.2112)
- **Original**: स्वजनेन 'च॑ संस्वक्तस्तेषु हार्दी तथाप्यति। एबमेंष सश्ाई अ द्वावष्यत्यन्तदु/खितो
- **Translation**: 

---

### Verse 13 (Markende Puran 0.2113)
- **Original**: दृष्टदोषेशपि विषये ममत्वाकृष्टरमानसी
- **Translation**: 

---

### Verse 14 (Markende Puran 0.2114)
- **Original**: त्त्किमेतन्महाभाग" यक्मोहों ज्ञानिनोरपि
- **Translation**: 

---

### Verse 15 (Markende Puran 0.2115)
- **Original**: ममास्य लव भवत्येपा विश्ेकान्थस्य मूछता
- **Translation**: 

---

### Verse 16 (Markende Puran 0.2116)
- **Original**: शजाने कड्ठा--
- **Translation**: 

---

### Verse 17 (Markende Puran 0.2117)
- **Original**: भगवन्‌! में आपसे एक थात पूछना चाहता हूँ, उसे बताइवे
- **Translation**: 

---

### Verse 18 (Markende Puran 0.2118)
- **Original**: मेरा चित्त अपने अधीन न होनेके कारण वह बात मेरे मनको बहुत दुःख देतों हैं। मुनिश्रेष्ठ। जो राज्य मेरें हाथसे चला गया है, उसमें और ठसके सम्पूर्ण अद्जॉमें मेरी ममता हो रहो है
- **Translation**: 

---

### Verse 19 (Markende Puran 0.2119)
- **Original**: यह जानते हुए भी कि बह अब मेरा नहीं है, अज्ञनौको भाँति मुझे उसके लिये दुःख होता है; यह क्या है? इधर यह वैश्य भी घरसे अपमानित होकर आया है। इसके पुत्र, स्त्रो और शुत्यॉमे इसको छोड़ दिया है
- **Translation**: 

---

### Verse 20 (Markende Puran 0.2120)
- **Original**: स्वजनोंने भी इसका यरित्याग कर दिया है, तो भी इसके इहृदयमें उनके प्रति अत्यन्त स्नेह है। इस प्रकार यह तथा मैं दोनों हो ऋघुत दुखी हैं
- **Translation**: 

---

