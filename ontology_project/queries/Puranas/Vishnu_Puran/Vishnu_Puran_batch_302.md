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

### Verse 1 (Vishnu Puran 0.6021)
- **Original**: 28 यज्ञाड्ुभूतं॑ यद्रुप॑ जगतः स्थितिसाधनम्‌। वृक्षादिभेदेष्यड्भेदि तस्मै मुख्यात्मने नमः
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.6022)
- **Original**: 29 तिर्यक्ष्मनुष्यदेवादिष्योमशब्दादिक॑ रूप तवादेः सर्वस्थ तस्मे सर्ात्यने नमः
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.6023)
- **Original**: 30 ते परमात्मन्‌ । रूपं॑ तवाद्ं यदनन्यतुल्य॑ ._तस्मे नमः कारणकारणाय
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.6024)
- **Original**: 39 कप ला यह्ध विशेषणानाम । रूपाय भ्रगवन्नताः सम:
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.6025)
- **Original**: 32 यनज्न: हशारीरेष यदन्यदेहे- . चशेषवस्तुष्रजमक्षय चत्त्‌। तस्माध्व नान्यद्व्यतिरिक्तमस्ति ब्रह्मस्वरूपाय नता: सम तस्मैं
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.6026)
- **Original**: 33 सकलमिदमजस्य यस्य रूप परमपदात्मवतस्सनातनस्य
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.6027)
- **Original**: प्रभुममलं प्रणतास्स्म बासुदेवम
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.6028)
- **Original**: 34 अ्रीपयाशर उवाच स्तोत्रस्थ चावसाने ते द्दृशु: परमेश्वरम्‌ । शद्भुचक्रगदापाणिं गरुडस्थं सुरा हरिम्‌
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.6029)
- **Original**: 35 रुद्र-ख्वरूपको नमस्कार है
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.6030)
- **Original**: रजोगुणकी प्रवृत्तिके कारण जो कमॉका करणरूप है, हे जनार्दन ! आपके उस मनुष्यात्मक स्वरूपक्ये नमस्कार है
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.6031)
- **Original**: हे सर्वात्मन्‌ ! जो अप्लाईस बध-युक्त* तमोमय और उन्मार्गगामी है आपके उस पश्ुरूपको नमस्कार है । 28
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.6032)
- **Original**: जो जगत्‌्की स्थितिका साधन और यज्ञका अगभृत है तथा वक्ष, खूता, गुल्म, वीरुघ, तृण और गिरि---इन छः: भेदोसे युक्त है उंन मुख्य (उद्धिद) रूप आपको नमस्कार है
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.6033)
- **Original**: तिर्यक्‌ मनुष्य तथा देता आदि प्राणी, आक्राशादि पशुधूत और चाव्दादि उनके गुण--ये सब, सबके आदिभूत आफ्हीके रूप हैं; अतः आप सर्जात्पाको नमस्कार है
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.6034)
- **Original**: हे परमात्मन्‌ ! प्रधान और महत्तत्त्वादिरूप इस सम्पूर्ण जगत्‌से जो परे है, सबका आदि कारण है तथा जिसके समान कोई अन्य रूप नहों है, आपके उस प्रकृति आदि कारणोंके भी कारण रूपको नमस्कार है
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.6035)
- **Original**: हे भगवन्‌ ! जो गुक्लादि रूपसे, दीर्घता आदि परिमाणसे तथा घनता आदि गुणोंसे रहित है, इस प्रकार जो समस्त विशेषणोंका अखिषय है तथा परमर्पषियोंका दर्शनोय एवं शुद्धातिशुद्ध है आपके उस स्वरूपकों हम नमस्कार करते हैं
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.6036)
- **Original**: जो हमारे शरीरोंमें, अन्य प्राणियोंके पारोरोपें तथा समस्त वस्तुऑमें वर्तमान है, अजभा और अचखिनाशी है तथा जिससे अतिरिक्त और कोई भी नहीं है, उस ब्रह्मस्वरूपकों हम नमस्कार करते हैं
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.6037)
- **Original**: परम पद ब्रह्म ही जिसका आत्पा है ऐसे जिस सनातन और अजतन्मा भगवान्‌का यह सकल प्रपञ्न रूप है, उस सबके बीजभूत, अविनाशी और निर्मल प्रभु वासुदेवको हम नमस्कार करते हैं
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.6038)
- **Original**: श्रीपरादरजी खोले--हे मैत्रेय ! स्तोत्रके समाप्त हो जानेपर देखताओंने परमात्मा श्रीहरिको हाथमें शल्ग, चक्र और गदा लिये तथा गरुढपर आरूढ़ हुए अपने सम्मुख विराजमान देखा
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.6039)
- **Original**: % श्यारह् इद्धिय-चथ, नौ तुष्टि-लध और आठ सिद्धि-लप--ये कुछ अड्डाईस वध हैं
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.6040)
- **Original**: इनका प्रधमांदा पशमाध्याय इत्म्रेक दसकी टिप्पणीमें जिस्तारपूर्बक वर्णन किया है।
- **Translation**: 

---

