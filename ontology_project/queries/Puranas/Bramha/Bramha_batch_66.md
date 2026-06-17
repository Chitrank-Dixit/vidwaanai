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

### Verse 1 (Bramha 0.1301)
- **Original**: हो आकाशमें स्थित तेजोराशि भगवान्‌ भास्करका निर्गुण एवं सनातन देवता बतलाया है; फिर
- **Translation**: 

---

### Verse 2 (Bramha 0.1302)
- **Original**: स्तवन करने लगीं। आपके ही मुँहसे हमने यह भी सुना है कि वे
- **Translation**: 

---

### Verse 3 (Bramha 0.1303)
- **Original**: अदिति बोलीं-- भगवन्‌ ! आप अत्यन्त सूक्ष्म, बारह स्वरूपोंमें प्रकट हुए। वे तेजकी राशि और
- **Translation**: 

---

### Verse 4 (Bramha 0.1304)
- **Original**: परम पवित्र और अनुपम तेज धारण करते हैं। महान्‌ तेजस्वी होकर किसी स्थत्रीके गर्भमें कैसे
- **Translation**: 

---

### Verse 5 (Bramha 0.1305)
- **Original**: तेजस्वियोंके ईश्वर, तेजके आधार तथा सनातन प्रकट हुए, इस विषयमें हमें बड़ा संदेह है।
- **Translation**: 

---

### Verse 6 (Bramha 0.1306)
- **Original**: देवता हैं। आपको नमस्कार है। गोपते ! जगत्‌का श्रह्माजी बोले--प्रजापति दक्षके साठ कन्याएँ
- **Translation**: 

---

### Verse 7 (Bramha 0.1307)
- **Original**: उपकार करनेके लिये मैं आपकी स्तुति--आपसे हुईं, जो श्रेष्ठ और सुन्दरी थीं। उनके नाम अदिति,
- **Translation**: 

---

### Verse 8 (Bramha 0.1308)
- **Original**: प्रार्था करती हूँ। प्रचण्ड रूप धारण करते दिति, दनु और विनता आदि थे। उनमेंसे तेरह
- **Translation**: 

---

### Verse 9 (Bramha 0.1309)
- **Original**: समय आपकी जैसी आकृति होती है, उसको मैँ कन्याओंका विवाह दक्षने कश्यपजीसे किया था।
- **Translation**: 

---

### Verse 10 (Bramha 0.1310)
- **Original**: प्रणाम करती हूँ । क्रमश: आठ मासतक पृथ्वीके अदितिने तीनों लोकोंके स्वामी देवताओंको जन्म
- **Translation**: 

---

### Verse 11 (Bramha 0.1311)
- **Original**: जलरूप रसको ग्रहण करनेके लिये आप जिस दिया। दितिसे दैत्य और दनुसे बलाभिमानी
- **Translation**: 

---

### Verse 12 (Bramha 0.1312)
- **Original**: अत्यन्त तीव्र रूपको धारण करते हैं, उसे मैं भयंकर दानव उत्पन्न हुए। विनता आदि अन्य
- **Translation**: 

---

### Verse 13 (Bramha 0.1313)
- **Original**: प्रणाम करती हूँ। आपका वह स्वरूप अग्नि और स्त्रियोंने भी स्थावर-जज्ज्म भूतोंको जन्म दिया।
- **Translation**: 

---

### Verse 14 (Bramha 0.1314)
- **Original**: सोमसे संयुक्त होता है। आप गुणात्माको नमस्कार इन दक्षसुताओंके पुत्र, पौत्र और दौहित्र आदिके
- **Translation**: 

---

### Verse 15 (Bramha 0.1315)
- **Original**: है। विभावसो! आपका जो रूप ऋक्‌, यजुष्‌ द्वारा यह सम्पूर्ण जगत्‌ व्याप्त हो गया। कश्यपके
- **Translation**: 

---

### Verse 16 (Bramha 0.1316)
- **Original**: और सामकी 'एकतासे त्रयीसंज्ञक इस विश्वके पुत्रोंमें देवता प्रधान हैं, वे सात्तिक हैं; इनके
- **Translation**: 

---

### Verse 17 (Bramha 0.1317)
- **Original**: रूपमें तपता है उसको नमस्कार है। सनातन! अतिरिक्त दैत्य आदि राजस और तामस हैं।
- **Translation**: 

---

### Verse 18 (Bramha 0.1318)
- **Original**: उससे भी परे जो '3&' नामसे प्रतिपादित स्थूल देवताओंको यज्ञका भागी बनाया गया है। परंतु
- **Translation**: 

---

### Verse 19 (Bramha 0.1319)
- **Original**: एवं सूक्ष्मरूप निर्मल स्वरूप है, उसको मेरा दैत्य और दानव उनसे शत्रुता रखते थे, अतः वे
- **Translation**: 

---

### Verse 20 (Bramha 0.1320)
- **Original**: प्रणाम है।* मिलकर उन्हें कष्ट पहुँचाने लगे। माता अदितिने
- **Translation**: 

---

