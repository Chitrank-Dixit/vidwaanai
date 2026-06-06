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

### Verse 1 (Mahabharat 0.521)
- **Original**: पुरीमें वे भगवान्‌ श्रीकृष्णके निज मन्दिरमें ही ठहरे और दोनों और योग्यताके अनुसार उनका अभिनन्दन किया। द्वारका-
- **Translation**: 

---

### Verse 2 (Mahabharat 0.521)
- **Original**: पुरीमें वे भगवान्‌ श्रीकृष्णके निज मन्दिरमें ही ठहरे और दोनों और योग्यताके अनुसार उनका अभिनन्दन किया। द्वारका-
- **Translation**: 

---

### Verse 3 (Mahabharat 0.522)
- **Original**: अनेक रात्रियोमें एक साथ ही सोये। कि औ-+ सुभद्राहरण और अभिमन्यु एवं प्रतिविन्ध्य आदि कुमारोंका जन्म वैज्वम्पायरजी कहते हैं--राजन्‌ ! एक बार वृष्णि, भोज
- **Translation**: 

---

### Verse 4 (Mahabharat 0.522)
- **Original**: अनेक रात्रियोमें एक साथ ही सोये। कि औ-+ सुभद्राहरण और अभिमन्यु एवं प्रतिविन्ध्य आदि कुमारोंका जन्म वैज्वम्पायरजी कहते हैं--राजन्‌ ! एक बार वृष्णि, भोज
- **Translation**: 

---

### Verse 5 (Mahabharat 0.523)
- **Original**: लिये युधिष्ठिस्के पास दूत भेजा । युभिष्ठिस्ने हर्षके साथ इस और अन्थक बंझोंके यादवोने रैवतक पर्वतपर बहुत बड़ा
- **Translation**: 

---

### Verse 6 (Mahabharat 0.523)
- **Original**: लिये युधिष्ठिस्के पास दूत भेजा । युभिष्ठिस्ने हर्षके साथ इस और अन्थक बंझोंके यादवोने रैवतक पर्वतपर बहुत बड़ा
- **Translation**: 

---

### Verse 7 (Mahabharat 0.524)
- **Original**: प्रस्तावका अनुमोदन किया। दूतके लौट आनेपर श्रीकृष्णने उत्सव मनाया। इस अवसरपर ब्राह्मणोंको हजारों सत्र और
- **Translation**: 

---

### Verse 8 (Mahabharat 0.524)
- **Original**: प्रस्तावका अनुमोदन किया। दूतके लौट आनेपर श्रीकृष्णने उत्सव मनाया। इस अवसरपर ब्राह्मणोंको हजारों सत्र और
- **Translation**: 

---

### Verse 9 (Mahabharat 0.525)
- **Original**: अर्जुनको वैसी सलाह दे दी। अपार सम्पत्तिका दान किया गया। यदुवंशी बालक सज-
- **Translation**: 

---

### Verse 10 (Mahabharat 0.525)
- **Original**: अर्जुनको वैसी सलाह दे दी। अपार सम्पत्तिका दान किया गया। यदुवंशी बालक सज-
- **Translation**: 

---

### Verse 11 (Mahabharat 0.526)
- **Original**: चडच्टचच्ट घजकर टहल रहे थे। अकूर; सारण; गद, वध; विदृरथ, पं त्वचा उद्धव, बलराम तथा अन्य प्रथान-प्रधान यदुबंधी अपनी-
- **Translation**: 

---

### Verse 12 (Mahabharat 0.526)
- **Original**: चडच्टचच्ट घजकर टहल रहे थे। अकूर; सारण; गद, वध; विदृरथ, पं त्वचा उद्धव, बलराम तथा अन्य प्रथान-प्रधान यदुबंधी अपनी-
- **Translation**: 

---

### Verse 13 (Mahabharat 0.527)
- **Original**: ु । अपनी पत्नियोंके साथ उत्सबकी झोभा बढ़ा रहे थे।
- **Translation**: 

---

### Verse 14 (Mahabharat 0.527)
- **Original**: ु । अपनी पत्नियोंके साथ उत्सबकी झोभा बढ़ा रहे थे।
- **Translation**: 

---

### Verse 15 (Mahabharat 0.528)
- **Original**: और बन्‍्दीजन उनका बिरद बख्ान रहे थे। गाजे-बाजे, नाच-
- **Translation**: 

---

### Verse 16 (Mahabharat 0.528)
- **Original**: और बन्‍्दीजन उनका बिरद बख्ान रहे थे। गाजे-बाजे, नाच-
- **Translation**: 

---

### Verse 17 (Mahabharat 0.529)
- **Original**: यहीं औकृष्णकी बहिन सुधद्रा भी थी। उसकी रूप-राझिसे भगवान्‌ कृष्णने अर्जुनके अभिष्रायको जानकर कहा कि सासबेली;क नि: है। इत्हो/कियेलओ, आर्य परकल/है।!
- **Translation**: 

---

### Verse 18 (Mahabharat 0.529)
- **Original**: यहीं औकृष्णकी बहिन सुधद्रा भी थी। उसकी रूप-राझिसे भगवान्‌ कृष्णने अर्जुनके अभिष्रायको जानकर कहा कि सासबेली;क नि: है। इत्हो/कियेलओ, आर्य परकल/है।!
- **Translation**: 

---

### Verse 19 (Mahabharat 0.530)
- **Original**: “ इक दिए सुण्याने वैवाका बदक क पज्टरेल अरके कह भगवान्‌ श्रीकृष्ण और अर्जुनने यह सल्मह करके अनुमतिके
- **Translation**: 

---

### Verse 20 (Mahabharat 0.530)
- **Original**: “ इक दिए सुण्याने वैवाका बदक क पज्टरेल अरके कह भगवान्‌ श्रीकृष्ण और अर्जुनने यह सल्मह करके अनुमतिके
- **Translation**: 

---

