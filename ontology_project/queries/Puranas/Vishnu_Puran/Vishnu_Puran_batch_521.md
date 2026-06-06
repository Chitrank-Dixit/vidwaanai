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

### Verse 1 (Vishnu Puran 0.10401)
- **Original**: पुत्रोंका मुख देखनेसे अत्यन्त उल्स्त्रस-सा प्राप्त होनेके
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.10402)
- **Original**: 366 विस्तारिताक्षियुगलो राजान्तःपुरयोषिताम्‌ । नागरस्त्रीसमूहश्न॒ ड्रछूं न विरराम तम्‌
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.10403)
- **Original**: 53 सख्यः पश्यत कृष्णस्य मुखमत्यरुणेक्षणम्‌ । गजयुद्धकृतायासस्वेदाग्बुकणिकाचितम्‌
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.10404)
- **Original**: 54 विकासिशर्दम्भोजमवश्यायजलोक्षितम्‌ । परिभूय स्थित जन्म सफल क्रियतां दृश:
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.10405)
- **Original**: 55 श्रीवत्साडु महद्धाम बालस्यैतद्विलोक्यताम्‌
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.10406)
- **Original**: विपक्षक्षपणं वक्षों भुजयुग्मं च भामिनि
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.10407)
- **Original**: 56 कि न पश्यसि दुग्धेन्दुमुणालधवल्लाकृतिम्‌ । बलभ्द्रमिमम नीलपरिधानमुपागतम्‌
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.10408)
- **Original**: 57 बलणता सुष्टिकेनेत चाण्रेण तथा सरित । क्रीडतो खलभद्रस्य हरेहास्पं तिलोक्यताम्‌
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.10409)
- **Original**: 58 सख्य: पश्यत चाणूरं नियुद्धार्थमयं हरि: । समुपैत्ति न सन्त्यत्र कि बृद्धा पुक्तकारिण:
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.10410)
- **Original**: 59 क् यौजनोन्मुखीभूतसुकुमारतनुहरि: । क्र क्‍ज्र॒कठिनाभोगशरीरोउयं॑ महासुर:
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.10411)
- **Original**: 60 इमो. सुललितैरहैयतेंते. नवयोवनो । द्ैतेयमल्लाओआरणूरप्रमुखास्त्वतिदारणा:
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.10412)
- **Original**: 61 नियुद्धप्राश्रिकानां तु महानेष व्यतिक्रम: । यदह्ालबलिनोर्युद्धं मध्यस्थैस्समुपेक्ष्यते
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.10413)
- **Original**: 62 औपराजर उदाय इत्थे पुरस्ील्लेकस्य वदतश्चालयन्भुवम्‌ । ववबल्ग बद्धकक्ष्योउन्तर्जनस्य भगवान्हरि:
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.10414)
- **Original**: 63 खलभद्रो5पि चास्फोल्ा बतल्ग ललित तथा । पदे पदे तथा भूमिर्यन्न शीर्णा तदद्धुतम्‌
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.10415)
- **Original**: 64 नियुद्धकुशलो दैत्यो बलभद्रेण मुष्टिकः
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.10416)
- **Original**: 65 सन्निपातावधूतैस्तु चाणूरेण सम॑ हरिः। अ्रक्षेपणर्मष्टिभिश्न कीलबज्जनिपातनै:
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.10417)
- **Original**: 66 अ्रीविष्णुपुराण [ अ0 20 कारण वसुदेवजी भी मानो आयी हुई जराकों छोड़कर फिरसे नत्रयूबक-से हो गये
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.10418)
- **Original**: राजाके अन्तःपुस्की स्लियाँ तथा नगर निवासिनी महिछलाएँ, भी उन्हें एकटक देखते-देखते उपराम न हुईं
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.10419)
- **Original**: [वे परस्पर कहने लूगीं---] “अरी सख्तियों ! अरुणनयनसे युक्त श्रीकृष्णचन्द्रका अति सुन्दर मुख तो देखो, जो कुबलयापौडके साथ युद्ध करनेके परिश्रमसे स्वेद ब्िन्दरपर्ण होकर हिस-कण-सिश्चित हारत्कालीन प्रफुल्ल कमछको लज्जित कर रहा है। अरी ! इसका दर्शन करके अपने नेत्रोंका होना सफल कर लो''
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.10420)
- **Original**: [एक ख््री बोली -- ] “हे भाभिनि ! इस बालकका यह लक्ष्मी आदिका आश्रयभूत श्रीवत्साकयुक्त वक्षःस्थऊक तथा झब्रुऑंको पराजित करनेवाल्जी इसकी दोनों भुजाएँ तो देखो !'
- **Translation**: 

---

