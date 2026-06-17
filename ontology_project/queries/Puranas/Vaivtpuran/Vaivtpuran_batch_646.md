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

### Verse 1 (Vaivtpuran 66.17883)
- **Original**: तथान्ते त्वं महामारी विश्वस्थ विश्वपूजिते । कालराश्रिम॑हारात्रिमोंहरात्रिश्न मोहिनी
- **Translation**: 

---

### Verse 2 (Vaivtpuran 66.17884)
- **Original**: दुरत्यया मे माया त्व॑ यया सम्मोहितं जगत्‌ । यया मुग्धो हि विद्वांक्ष मोक्षमार्ग न पश्यति
- **Translation**: 

---

### Verse 3 (Vaivtpuran 66.17885)
- **Original**: इत्यात्मना कृतं स्तोत्र दुर्गाया दुर्गनगाशनम्‌ । पूजाकाले पठेद्‌ यों हि सिद्धिर्भवति वाजिछता
- **Translation**: 

---

### Verse 4 (Vaivtpuran 66.17886)
- **Original**: वन्ध्याच काकवन्ध्या च मृतवत्सा च दुर्भगा । श्रुत्वा स्तोत्र वर्षमेक॑ सुपुत्र लभते शध्रुवम्‌
- **Translation**: 

---

### Verse 5 (Vaivtpuran 66.17887)
- **Original**: कारागारे महाघोरे यो बद्धों दृढबन्धने । श्रुत्वा स्तोत्र मासमेक बन्धनान्मुच्यते ध्रुवम्‌
- **Translation**: 

---

### Verse 6 (Vaivtpuran 66.17888)
- **Original**: यक्ष्गग्रस्तो गलत्कुष्ठी महाशूली महाज्वरी । श्रुत्वा स्तोत्र वर्षमेक॑ सद्यो रोगातू प्रमुच्यते
- **Translation**: 

---

### Verse 7 (Vaivtpuran 66.17889)
- **Original**: पुत्रभेदे प्रजाभेदे पलीधेदे च॒ दुर्गतः । श्रुत्वा स्तोत्र मासमे्क लभते नात्र संशय:
- **Translation**: 

---

### Verse 8 (Vaivtpuran 66.17890)
- **Original**: राजद्वरे श्मशाने च॑ महारण्ये रणस्थले । हिंस्नजन्तुसमीपे च॒ श्रुत्या स्तोत्र प्रमुच्यते
- **Translation**: 

---

### Verse 9 (Vaivtpuran 66.17891)
- **Original**: गृहदहे च दावाग्नौ दस्युसैन्यसमन्विते । स्तोत्रअ्रवणमात्रेण लभते नात्र संशयः
- **Translation**: 

---

### Verse 10 (Vaivtpuran 66.17892)
- **Original**: महादरिद्रो मूर्खश्च वर्ष स्तोत्र पठेत्तु यः । विद्यावान्‌ धनवांश्ैव स॒भवेन्नात्र संशय:
- **Translation**: 

---

### Verse 11 (Vaivtpuran 66.17893)
- **Original**: इति औरीब्रह्मवैवर्ते श्रीकृष्णकृत॑ दुर्गास्तोत्रं सम्पूर्णमू। (प्रकृतिखण्ड 66। 7-33) #00#00/>न्येप;9+-20002 परशुरामकृतं दुर्गास्तोत्रम्‌ परशुराम उवाच श्रीकृष्णस्य च गोलोके परिपूर्णतमस्य च। आविर्भूता विग्रहतः पुरा सृष्टयुन्मुखस्थ च
- **Translation**: 

---

### Verse 12 (Vaivtpuran 66.17894)
- **Original**: सूर्यकोटिप्रभायुक्ता वस्त्रालंकारभूषिता । वह्लिशुद्धांशुकाधाना सुस्मिता सुमनोहरा
- **Translation**: 

---

### Verse 13 (Vaivtpuran 66.17895)
- **Original**: नवयौवनसम्पन्ना सिन्दूरविन्दुशोभिता । ललितं कबरीभारं मालतीमाल्यमणिडतम्‌
- **Translation**: 

---

### Verse 14 (Vaivtpuran 66.17896)
- **Original**: अहोउनिर्वचनीया त्व॑ चारुमूति च बिशभ्रती । मोक्षप्रदा मुमुक्षूणां महाविष्णोर्विधि: स्वयम्‌
- **Translation**: 

---

### Verse 15 (Vaivtpuran 66.17897)
- **Original**: मुमोह क्षणमात्रेण दृष्ठा त्वां सर्वमोहिनीम्‌ । खालै: सम्भूय सहसा सस्मिता धाविता पुरा
- **Translation**: 

---

### Verse 16 (Vaivtpuran 66.17898)
- **Original**: सद्धिः ख्याता तेन राथा मूलप्रकृतिरीक्षती । कृष्णस्त्वां सहसाहूब वीर्याधान॑ चकार ह
- **Translation**: 

---

### Verse 17 (Vaivtpuran 66.17899)
- **Original**: ततो डिम्भं॑ महज्जज्ञे ततो जातो महाविराद । यस्यैबव लोमकूपेषु ब्रह्माण्डान्यखिलानि अऊऋ
- **Translation**: 

---

### Verse 18 (Vaivtpuran 66.17900)
- **Original**: तच्छुड्ारक्रमेणैव. त्वन्नि:श्ासों बभूव ह
- **Translation**: 

---

### Verse 19 (Vaivtpuran 66.17901)
- **Original**: स निःश्वासों महावायु: स विराड्‌ विश्वधारक:
- **Translation**: 

---

### Verse 20 (Vaivtpuran 66.17902)
- **Original**: तव॒ घर्मजलेनैव पुप्लुवे विश्वनोलकम्‌ । स॒विराड्‌ विश्वनिलयो जलराशिर्बभूव ह
- **Translation**: 

---

