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

### Verse 1 (Bramha 0.81)
- **Original**: जो धर्मके तत्त्वकों बिलकुल नहीं समझता था। और आयुकी वृद्धि करनेवाला, परम धन्य, वेदोंके
- **Translation**: 

---

### Verse 2 (Bramha 0.82)
- **Original**: उसका जन्म मृत्युकन्या सुनीधाके गर्भसे हुआ था।
- **Translation**: 

---

### Verse 3 (Bramha 0.83)
- **Original**: अपने नानाके स्वभावदोषके कारण वह धर्मकों !' करनेबाला इस भूतलपर कौन है? मैं ही सम्पूर्ण पीछे रखकर काम और लोभमें प्रवृत्त हो गया।
- **Translation**: 

---

### Verse 4 (Bramha 0.84)
- **Original**: प्राणियोंकी और विशेषत: सब धर्मोकी उत्पत्तिका उसने धर्मकी मर्यादा भज्ग कर दी और बैदिक
- **Translation**: 

---

### Verse 5 (Bramha 0.85)
- **Original**: कारण हूँ। तुम सब लोग मूर्ख और अचेत हो, धर्मोका उल्लब्बन करके वह अधर्ममें तत्पर हो
- **Translation**: 

---

### Verse 6 (Bramha 0.86)
- **Original**: इसलिये मुझे नहीं जानते। यदि मैं चाहूँ तो इस गया। विनाशकाल उपस्थित होनेके कारण उसने
- **Translation**: 

---

### Verse 7 (Bramha 0.87)
- **Original**: पृथ्वीको भस्म कर दूँ, जलपें बहा दूँ या भूलोक यह क़ूर प्रतिज्ञा कर ली थी कि 'किसीको यज्ञ
- **Translation**: 

---

### Verse 8 (Bramha 0.88)
- **Original**: तथा द्युतोकको भी रूँध डालूँ। इसमें तनिक भी और होम नहीं करने दिया जायगा। यजन करने
- **Translation**: 

---

### Verse 9 (Bramha 0.89)
- **Original**: अन्यथा विचार करनेकी आवश्यकता नहीं है।' योग्य, यज्ञ करनेवाला तथा यज्ञ भी मैं ही हूँ। मेरे
- **Translation**: 

---

### Verse 10 (Bramha 0.90)
- **Original**: जब महर्षिगण वेनको मोह और अहड्भारसे किसी ही लिये यज्ञ करना चाहिये। मेरे ही उद्देश्यसे
- **Translation**: 

---

### Verse 11 (Bramha 0.91)
- **Original**: तरह हटा न सके, तब उन्हें बड़ा क्रोध हुआ। उन हवन होना चाहिये।' इस प्रकार मर्यादाका उल्लद्वन
- **Translation**: 

---

### Verse 12 (Bramha 0.92)
- **Original**: महात्माओंने महाबली वेनको पकड़कर बाँघ करके सब कुछ ग्रहण करनेवाले अयोग्य वेनसे
- **Translation**: 

---

### Verse 13 (Bramha 0.93)
- **Original**: लिया। उस समय वह बहुत उछल-कूद मचा रहा मरीचि आदि सब महर्षियोंने कहा-'खेन! हम , था। महर्षि कुपित तो थे ही, वेनकी बायीं अनेक यर्षोंके लिये यज्ञकी दीक्षा ग्रहण करनेवाले
- **Translation**: 

---

### Verse 14 (Bramha 0.94)
- **Original**: जद्भाका मन्धन करने लगे। इससे एक काले हैं। तुम अधर्म न करों। यह यज्ञ आदि कार्य रंगका पुरुष उत्पन्न हुआ, जो बहुत ही नाटा था। सनातन धर्म है। यह भयभीत हो हाथ जोड़कर खड़ा हो गया। उसे महर्षियोंको यों कहते देख खोटी बुद्धिबाले व्याकुल देख अश्रिने कहा-“निषीद (बैठ जा)। 1 (0 । इससे वह निषादवंशका प्रवर्तक हुआ और बेनके
- **Translation**: 

---

### Verse 15 (Bramha 0.95)
- **Original**: 5 पापसे उत्पन्न हुए धीवरोंकी सृष्टि करने लगा। तत्पश्चात्‌ महात्माओंने पुन: अरणीको भाँति वेनकी बेनने हँसकर कहा--' अरे ! मेरे सिवा दूसरा कौन
- **Translation**: 

---

### Verse 16 (Bramha 0.96)
- **Original**: द् रह रा! धर्मका स्ष्टा है। मैं किसको बात सुतं। विद्या,
- **Translation**: 

---

### Verse 17 (Bramha 0.97)
- **Original**: £“+ है 23 >छ पराक्रप, तपस्या और सत्यके द्वारा मेरो समानता
- **Translation**: 

---

### Verse 18 (Bramha 0.98)
- **Original**: 6 * संक्षिप्त ब्रह्मपुराण « दाहिनी भुजाका मन्थन किया। उससे अग्निके
- **Translation**: 

---

### Verse 19 (Bramha 0.99)
- **Original**: हैं।' यह सुनकर सूत और मागधने उन महर्षियोंसे समान तेजस्थी पृथुका प्रादुर्भाव हुआ। वे भयानक
- **Translation**: 

---

### Verse 20 (Bramha 0.100)
- **Original**: कहा--'हम अपने कर्मोंसे देवताओं तथा ऋषियोंको टंकार करनेवाले आजगब नामक धनुष, दिव्य प्रसन्‍त करते हैं। इन महाराजका नाम, कर्म, बाण तथा रक्षार्थ कवच धारण किये प्रकट हुए
- **Translation**: 

---

