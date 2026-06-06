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

### Verse 1 (Vaivtpuran 13.11122)
- **Original**: संत-महात्मा भी आपकी स्तुतिके विषयमें रोने लगे। कोई भाग गये और कोई डरके मारे
- **Translation**: 

---

### Verse 2 (Vaivtpuran 13.11123)
- **Original**: शक्तिहीनताका ही परिचय देते हैं। कहाँ तो मैं बिलमें घुस गये। अपने प्रियतमको मरणोन्मुख
- **Translation**: 

---

### Verse 3 (Vaivtpuran 13.11124)
- **Original**: कुबुद्धि, अज्ञ एवं नारियोंमें अधम सर्पिणी और हुआ देख नागपत्री सती सुरसा दूसरी नागिनियोंके
- **Translation**: 

---

### Verse 4 (Vaivtpuran 13.11125)
- **Original**: कहाँ सम्पूर्ण भुवनोंके परम आश्रय तथा किसीके साथ त्रीहरिके सामने आयी और पति-प्रेमसे रोने
- **Translation**: 

---

### Verse 5 (Vaivtpuran 13.11126)
- **Original**: भी दृष्टिपथमें न आनेवाले आप परमेश्वर! जिनकी लगी। उसने दोनों हाथ जोड़कर शीघ्र ही भयसे
- **Translation**: 

---

### Verse 6 (Vaivtpuran 13.11127)
- **Original**: स्तुति ब्रह्मा, विष्णु और शेषनाग करते हैं, उन श्रीहरिको प्रणाम किया और उनके दोनों चरणारविन्द
- **Translation**: 

---

### Verse 7 (Vaivtpuran 13.11128)
- **Original**: मानव-वेषधारी आप नराकार परमेश्वरकी स्तुति मैं पकड़कर व्याकुल हो उनसे कहा। करना चाहती हूँ, यह कैसी विडम्बना है? पार्वती, सुरसा बोली--हे जगदीश्वर! आप मुझे मेरे [लक्ष्मी तथा वेदजननी सावित्री जिनके स्तवनसे स्वामीको लौटा दीजिये। दूसरोंकों मान देनेवाले
- **Translation**: 

---

### Verse 8 (Vaivtpuran 13.11129)
- **Original**: डरती हैं और स्तुति करनेमें समर्थ नहीं हो पातीं; प्रभो! मुझे भी मान दीजिये। स्त्रियोंको पति
- **Translation**: 

---

### Verse 9 (Vaivtpuran 13.11130)
- **Original**: उन्हीं आप परमेश्वरका स्तवन कलिकलुषमें निमग्र प्राणोंसे भी बढ़कर प्रिय होता है। उनके लिये
- **Translation**: 

---

### Verse 10 (Vaivtpuran 13.11131)
- **Original**: तथा बेद-वेदाज् एवं शास्त्रोंके श्रवणमें मूढ़ स्त्री पतिसे बढ़कर दूसरा कोई बन्धु नहीं है। नाथ!
- **Translation**: 

---

### Verse 11 (Vaivtpuran 13.11132)
- **Original**: मैं क्यों करना चाहती हूँ, यह समझमें नहीं आता। आप देवेश्वरोंके भी स्वामी, अनन्त प्रेमके सागर,
- **Translation**: 

---

### Verse 12 (Vaivtpuran 13.11133)
- **Original**: आप रलत्रमय पर्यक्कूपर र्ननिर्मित भूषणोंसे भूषित हो शयन करते हैं। रत्नालंकारोंसे अलंकृत अज्जवाली “24
- **Translation**: 

---

### Verse 13 (Vaivtpuran 13.11134)
- **Original**: राधिकाके वक्ष:स्थलपर विराजमान होते हैं। आपके ;
- **Translation**: 

---

### Verse 14 (Vaivtpuran 13.11135)
- **Original**: सम्पूर्ण अड्र चन्दनसे चर्चित रहते हैं, मुखारविन्दपर
- **Translation**: 

---

### Verse 15 (Vaivtpuran 13.11136)
- **Original**: मन्द मुस्कानकी प्रभा फैली होती है। आप उमड़ते 93 5 हुए प्रेमरसके महासागरमें सदा सुखसे निमग्र रहते 4
- **Translation**: 

---

### Verse 16 (Vaivtpuran 13.11137)
- **Original**: हैं। आपका मस्तक मल्लिका और मालतीकी मालाओंसे सुशोभित होता है। आपका मानस 5
- **Translation**: 

---

### Verse 17 (Vaivtpuran 13.11138)
- **Original**: नित्य निरन्तर पारिजात पुष्पोंकी सुगन्‍्धसे आमोदित 95) रहा करता है। कोकिलके कलरव तथा भ्रमरोंके 2 लक, हे गुझ्लारवसे उद्दीपित प्रेमके कारण आपके अड्ज 27352. >4&& 4:
- **Translation**: 

---

### Verse 18 (Vaivtpuran 13.11139)
- **Original**: उठी हुई पुलकावलियोंसे अलंकृत रहते हैं। जो उत्तम बन्धु, सम्पूर्ण भुवनोंके बान्धव तथा! सदा प्रियतमाके दिये हुए ताम्बूलका सानन्द
- **Translation**: 

---

### Verse 19 (Vaivtpuran 13.11140)
- **Original**: 496 * संक्षिप्त ब्रह्मवैवर्तपुराण * #%###%#%#####%ऊऋ%ऊ% कक ऋऋऋऋऋ कक # 4 4 कक. कं्क््रंकऋ् ऋऋ्कऋऋऋऋ ऋऋऋ कक ऋऋऋ##
- **Translation**: 

---

### Verse 20 (Vaivtpuran 13.11141)
- **Original**: ##%# # ## # # चर्वण करते हैं; वेद भी जिनकी स्तुति करनेमें
- **Translation**: 

---

