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

### Verse 1 (Vaivtpuran 29.7418)
- **Original**: +* गणपतिखण्ड + 357 शिवजीका परशुरामको मन्त्र, ध्यान, पूजाविधि और स्तोत्र प्रदान करना परशुरामने कहा--नाथ ! जो सम्पूर्ण अज्लोंकी
- **Translation**: 

---

### Verse 2 (Vaivtpuran 29.7419)
- **Original**: नम: श्रीकृष्णाय परिपूर्णतमाय स्वाहा ' यह सप्तदशाक्षर रक्षा करनेवाला, सुखदायक, मोक्षप्रद, सारसर्वस्व
- **Translation**: 

---

### Verse 3 (Vaivtpuran 29.7420)
- **Original**: महामन्त्र सभी मन्त्रोंमें मन्त्रराज है। मुनिवर! पाँच तथा शत्रुओंके संहारका कारण है, वह कवच तो
- **Translation**: 

---

### Verse 4 (Vaivtpuran 29.7421)
- **Original**: लाख जप करनेसे यह मन्त्र सिद्ध हो जाता है। मुझे प्राप्त हो गया। सामर्थ्यशाली भगवन्‌! अब
- **Translation**: 

---

### Verse 5 (Vaivtpuran 29.7422)
- **Original**: उस समय जपका दशांश हवन, हवनका दशांश मुझ अनाथको मन्त्र, स्तोत्र और पूज़ाबिधि प्रदान
- **Translation**: 

---

### Verse 6 (Vaivtpuran 29.7423)
- **Original**: अभिषेक, अभिषेकका दशांश तर्पण और तर्पणका कीजिये; क्योंकि आप शरणागतके पालक हैं।
- **Translation**: 

---

### Verse 7 (Vaivtpuran 29.7424)
- **Original**: दशांश मार्जन करनेका विधान है तथा सौ मोहरें महादेवजी बोले--भूृगुनन्दन! '3& श्रीं
- **Translation**: 

---

### Verse 8 (Vaivtpuran 29.7425)
- **Original**: इस पुरश्षणणकी दक्षिणा बतायी गयी हैं। मुने! यद्‌ धृत्वा जगतां साक्षी धर्मो धर्मभृतां वर: । सर्वविद्याधिदवी सा यक्वच धृत्वा सरस्वती
- **Translation**: 

---

### Verse 9 (Vaivtpuran 29.7426)
- **Original**: यदू धृत्वा जगतां लक्ष्मीरम्रदात्री परात्परा
- **Translation**: 

---

### Verse 10 (Vaivtpuran 29.7427)
- **Original**: यंद्‌ धृत्वा पठनाद्‌ वेदान्‌ सावित्री प्रसुषाव च
- **Translation**: 

---

### Verse 11 (Vaivtpuran 29.7428)
- **Original**: वेदाश्ल॒ धर्मबछारों यद्‌ धृत्वा पठनाद्‌ भृगों। यद्‌ धृत्वा पठनाच्छुद्धस्तेजस्वी हव्यवाहन:
- **Translation**: 

---

### Verse 12 (Vaivtpuran 29.7429)
- **Original**: सनत्कुमारें भगवान्‌ यद्‌ धूृत्वा ज्ञानिनां वर: । दातव्यं कृष्णभक्तायः साधवे च महात्मने
- **Translation**: 

---

### Verse 13 (Vaivtpuran 29.7430)
- **Original**: शठाय परशिष्याय. दत्वा. मृत्युमवाघ्रुयात्‌ । जैलोक्यविजयस्यास्थ कवचस्य प्रजापति:
- **Translation**: 

---

### Verse 14 (Vaivtpuran 29.7431)
- **Original**: ऋषिश्छन्दक्ष॒ गायत्री देवो रासेश्व: स्वयम्‌ । जैलोक्यविजयप्राप्ता विनियोग: . प्रकीर्तित:
- **Translation**: 

---

### Verse 15 (Vaivtpuran 29.7432)
- **Original**: परात्परं च कवच त्रिषपु लोकेषु दुर्लभम्‌ । प्रणबों मे शिरः पातु श्रीकृष्णाय नमः: सदा
- **Translation**: 

---

### Verse 16 (Vaivtpuran 29.7433)
- **Original**: सदा पायात्‌ कपाल॑ कृष्णाय स्वाहेति पञ्माक्षःः । कृष्णेति पातु नेत्रे च कृष्णस्वाहेति तारकम्‌
- **Translation**: 

---

### Verse 17 (Vaivtpuran 29.7434)
- **Original**: हरये नम हत्येव॑ भ्रूलतां पातु में सदा। 3$ गोविन्दाय स्वाहेति नासिकां पातु संततम्‌
- **Translation**: 

---

### Verse 18 (Vaivtpuran 29.7435)
- **Original**: गोपालाय नमों गण्डौ पातु में सर्वतः सदा । 3» नमो गोपाडुनेशाय कर्णा पातु सदा मम
- **Translation**: 

---

### Verse 19 (Vaivtpuran 29.7436)
- **Original**: 3$ कृष्णाय नमः शश्वत्‌ पातु मे5धरयुग्मकमम्‌
- **Translation**: 

---

### Verse 20 (Vaivtpuran 29.7437)
- **Original**: 3* गोविन्दाय स्वाहेति दन्तावलिं में सदावतु
- **Translation**: 

---

