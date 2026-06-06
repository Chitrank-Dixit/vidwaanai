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

### Verse 1 (Vaivtpuran 543.15754)
- **Original**: नहीं होता; क्योंकि स्वयं राधा मेरी गोदमें रहती 6
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.15755)
- **Original**: हैं और उनकी छाया रायाणकी भार्या होती है। 2
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.15756)
- **Original**: . इस प्रकार भगवान्‌ विष्णुके वचनकों सुनकर मूर्तिने कहा--हे नाथ! आप तो करुणासागर
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.15757)
- **Original**: सुन्दरी वृन्दाने धर्मको अपनी आयु प्रदान कर हैं। दीनबन्धो ! मुझपर कृपा कीजिये। कृपामूर्ति
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.15758)
- **Original**: दी। फिर तो धर्म पूर्णरूपसे उठकर खड़े हो जगन्नाथ! मेरे पतिदेवकों शीघ्र जीवित कर
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.15759)
- **Original**: गये। उनके शरीरकौ कान्ति तपाये हुए सुवर्णकी दीजिये; क्योंकि जो नारी पतिसे हीन हो जाती
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.15760)
- **Original**: भाँति चमक रही थी और उनका सौन्दर्य पहलेकी है, वह इस भवसागरमें पापिनी समझो जाती
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.15761)
- **Original**: अपेक्षा बढ़ गया था। तब उन श्रीमानने परात्पर है। उसकी दशा नेत्रहीन मुख और प्राणरहित
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.15762)
- **Original**: परमेश्वरको प्रणाम किया। शरीरके समान हो जाती है। माता-पिता, भाई- पुनः बृन्दाने कहा--देवगण मेरे वचनको, बन्धु और पुत्र तो परिमित सुख देनेवाले होते
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.15763)
- **Original**: जिसका उल्लड्लडन करना कठिन है, सावधानतया हैं, सर्वस्व प्रदान करनेवाला तो सामर्थ्यशाली
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.15764)
- **Original**: श्रवण करें। मेरा वाक्य मिथ्या नहीं हो सकता। पति हो होता है।--इतना कहकर मूर्ति देवी
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.15765)
- **Original**: मैंने क्रोधावेशमें जो तीन बार “क्षयों भव', वहाँ खडो हो गयीं और बिलाप करने लगीं। 'तुम्हारा नाश हो जाय'--ऐसा वचन कहा है और तब भगवान्‌, जो सर्वात्मा एवं प्रकृतिसे परे हैं;
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.15766)
- **Original**: पुनः कहनेके लिये उद्यत होनेपर सूर्यने मना कर वृन्दासे बोले। दिया था, उसका फल यों होगा-यह धर्म श्रीभगवानने कहा--सुन्दरि! तुमने तपस्याद्वारा
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.15767)
- **Original**: सत्ययुगमें जैसे पहले परिपूर्ण था, उसी तरह इस ब्रह्मकी आयुके समान आयु प्राप्त की है। वह
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.15768)
- **Original**: समय भी रहेगा; परंतु त्रेतामें इसके तीन पैर, अपनी आयु तुम धर्मको दे दो और स्वयं द्वापरमें दो पैर और कलियुगके प्रथमांशमें एक पैर गोलोककों चली जाओ। वहाँ तुम तपस्याके
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.15769)
- **Original**: रह जायगा। कलियुगके शेष भागमें यह कलाका प्रभावसे इसी शरीरद्वारा मुझे प्राप्त करोगी।
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.15770)
- **Original**: घषोडशांशमात्र रह जायगा। सत्ययुग आनेपर यह सुमुखि
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.15771)
- **Original**: गोलोकमें आनेफे पश्चात्‌ वाराहकल्पमें
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.15772)
- **Original**: पुनः परिपूर्ण हो जायगा। मेरे मुखसे तीन बार तुम राधाकी छायाभूता वृषभानुकी कन्या होओगी।
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.15773)
- **Original**: क्षय' शब्द निकला है; इसलिये उसी क्रमसे क्षय उस समय मेरे कलांशसे उत्पन्न हुए ऱायाण गोप
- **Translation**: 

---

