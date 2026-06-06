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

### Verse 1 (Vaivtpuran 16.3234)
- **Original**: (प्रकृतिखण्ड 16। 114)
- **Translation**: 

---

### Verse 2 (Vaivtpuran 16.3235)
- **Original**: करने लगे। तब विधाता ब्रह्मा देवताओंकों साथ
- **Translation**: 

---

### Verse 3 (Vaivtpuran 16.3236)
- **Original**: रत्नमय दर्पणोंसे वह सभा सुशोभित थी। उसकी लेकर भगवान्‌ शंकरके स्थानपर गये। वहाँ
- **Translation**: 

---

### Verse 4 (Vaivtpuran 16.3237)
- **Original**: दीवारोंमें लिखित अनेक प्रकारके विचित्र चित्र पहुँचकर मस्तकपर चन्द्रमाकों धारण करनेवाले
- **Translation**: 

---

### Verse 5 (Vaivtpuran 16.3238)
- **Original**: उसकी सुन्दरता बढ़ा रहे थे। सर्वोत्कृष्ट पद्मराग- सर्वेश शिवसे सभी बातें कह सुनायीं। फिर
- **Translation**: 

---

### Verse 6 (Vaivtpuran 16.3239)
- **Original**: मणिसे निर्मित कृत्रिम कमलोंसे बह परम ब्रह्मा और शंकर देवताओंको साथ लेकर
- **Translation**: 

---

### Verse 7 (Vaivtpuran 16.3240)
- **Original**: सुशोभित थी। स्यमन्तकमणिसे बनी हुई सैकड़ों वैकुण्ठके लिये प्रस्थित हुए। वैकुण्ठ परम धाम
- **Translation**: 

---

### Verse 8 (Vaivtpuran 16.3241)
- **Original**: सीढ़ियाँ उस भवनकी शोभा बढ़ाती थीं। रेशमकी है। यह सबके लिये दुर्लभ है। वहाँ बुढ़ापा
- **Translation**: 

---

### Verse 9 (Vaivtpuran 16.3242)
- **Original**: डोरीमें गुँथे हुए दिव्य चन्दन-वृक्षके सुन्दर पह्लव और मृत्युका प्रभाव नहीं है। भगवान्‌ श्रीहरिके
- **Translation**: 

---

### Verse 10 (Vaivtpuran 16.3243)
- **Original**: वन्दनवारका काम दे रहे थे। यहाँके खंभोंका भवनका प्रवेशद्वार परम श्रेष्ठ है। वहाँ पहुँचकर
- **Translation**: 

---

### Verse 11 (Vaivtpuran 16.3244)
- **Original**: निर्माण इन्द्रनील-मणिसे हुआ था। उत्तम रत्रोंसे रत्रमय सिंहासनपर बैठे हुए द्वारपालॉंको जब
- **Translation**: 

---

### Verse 12 (Vaivtpuran 16.3245)
- **Original**: भरे कलशोंसे संयुक्त वह सभा अत्यन्त मनोरम देखा, तब इन ब्रह्मादि देवताओंका मन आश्चर्यसे
- **Translation**: 

---

### Verse 13 (Vaivtpuran 16.3246)
- **Original**: जान पड़ती थी। पारिजात-पुष्पोंके बहुत-से हार भर गया। वे सभी परम सुन्दर थे। सभी उसे अलंकृत किये हुए थे। कस्तूरी एवं कुक्कूमसे पीताम्बर धारण किये हुए थे। रत्रमय आभूषणोंसे
- **Translation**: 

---

### Verse 14 (Vaivtpuran 16.3247)
- **Original**: युक्त सुगन्धपूर्ण चन्दनके द्रवसे वह भवन विभूषित थे। सबके गलेमें दिव्य बनमाला लहरा
- **Translation**: 

---

### Verse 15 (Vaivtpuran 16.3248)
- **Original**: सुसब्जित तथा सुसंस्कृत किया गया था। सुगन्धित रही थी; सुन्दर शरीर श्याम रंगके थे। उनके
- **Translation**: 

---

### Verse 16 (Vaivtpuran 16.3249)
- **Original**: वायुसे वह सभा सब ओरसे सुवासित थी। उसका शह्कलु, चक्र, गदा और पड़ासे सुशोभित चार
- **Translation**: 

---

### Verse 17 (Vaivtpuran 16.3250)
- **Original**: विस्तार एक सहस्र योजन था। सर्वत्र सेवक खड़े भुजाएँ थीं और प्रसन्न बदन मुस्कानसे भरे थे।
- **Translation**: 

---

### Verse 18 (Vaivtpuran 16.3251)
- **Original**: थे। वहाँ सभी कुछ दिव्य था। सभी उस उन मनोहर द्वारपालोंके नेत्र कमलके सदृश
- **Translation**: 

---

### Verse 19 (Vaivtpuran 16.3252)
- **Original**: सभाभवनको देखकर मुग्ध हो गये। विशाल थे। नारद! भगवान्‌ श्रीहरि उस अनुपम सभाके उन द्वारपालोंसे अनुमति पाकर ब्रह्मा क्रमशः
- **Translation**: 

---

### Verse 20 (Vaivtpuran 16.3253)
- **Original**: मध्य भागमें इस प्रकार विराजमान थे मानो सोलह द्वारोंको पार करके भगवान्‌ श्रीहरिकी
- **Translation**: 

---

