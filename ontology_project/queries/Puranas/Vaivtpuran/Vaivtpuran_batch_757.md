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

### Verse 1 (Vaivtpuran 543.13454)
- **Original**: कर रहा है। इसलिये मैं शाप देती हूँ कि कहाीं। उन्हें सुनकर पद्मा बोली--'ओ पापिष्ट कालक्रमसे तेरा क्षय हो जायगा।'
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.13455)
- **Original**: 84 + संक्षिप्त ग्रह्मवैयर्तपुराण « अफडऊ& 4 ऋ 8 ऋ कक ऋ# # 4 8 ऋ ऋ #ऋ 4 8 ऋ 8 धक ऋ कक ## % 4 # 8 # #% 64% #% #£ # 6 % # # # % 4 # # % ## 8 4 ऋ ध# # ऋ 5 इक सतीका शाप सुनकर देवेश्वर धर्म काँपने
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.13456)
- **Original**: एवं निर्गुण हैं; उन भगवान्‌ श्रीकृष्णको नमस्कार लगे और राजाका रूप छोड़ अपनी मूर्ति धारण
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.13457)
- **Original**: है और जो सर्वरूप, सर्वबीजस्वरूप, सबके करके उससे बोले। अन्तरात्मा तथा समस्त जीवोंके लिये बन्धुस्वरूप धर्मने कहा--मात:! आप मुझे धर्मज्ञोंके
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.13458)
- **Original**: हैं; उन भगवान्‌ श्रीकृष्णको नमस्कार है। गुरुका भी गुरु धर्म समझिये। पतिक्रते! मैं सदा यों कहकर जगदुरु धर्म पद्माके सामने खड़े परायी स्त्रीके प्रति माताका ही भाव रखता हूँ। हो गये। शैलराज! धर्मका परिचय पाकर वह मैं आपके आन्तरिक भावको समझनेके लिये ही
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.13459)
- **Original**: साध्वी सहसा बोल उठी। आया था। यद्यपि आप-जैसी सतियोंका मन कैसा पद्माने कहा-- भगवन्‌ ! क्या आप ही सबके होता है, यह मैं जानता था; तथापि दैवसे प्रेरित
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.13460)
- **Original**: समस्त कर्मोंके साक्षी, सबके भीतर रहनेवाले, होकर परीक्षा करनेके लिये चला आया। साध्वि!
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.13461)
- **Original**: सर्वात्मा, सर्वज्ञ तथा सर्वतत्त्ववेत्ता धर्म हैं? फिर आपने जो मेरा दमन किया है, वह नीतिके विरुद्ध
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.13462)
- **Original**: मेरे मनको जाननेके लिये मुझ दासीकी विडम्बना नहीं है; सर्वथा उचित ही है; क्योंकि कुमार्गपर
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.13463)
- **Original**: क्‍यों करते हैं? धर्मदेव ! आपके प्रति मैंने जो कुछ चलनेवालोंके लिये दण्डका विधान साक्षात्‌
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.13464)
- **Original**: किया है, वह मेरा अपराध है। प्रभो! मैंने स्त्री- परमेश्वर श्रीकृष्णने ही किया है। जो धर्मको भी
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.13465)
- **Original**: स्वभाववश आपको न जाननेके कारण क्रोधपूर्वक स्वधर्मका ज्ञान कराने और कालकी भी कलना
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.13466)
- **Original**: शाप दे दिया है। उस शापकी क्या व्यवस्था होगी; (गणना) तथा स्रष्टाकी भी सृष्टि करनेमें समर्थ
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.13467)
- **Original**: यही इस समय मेरा चिन्ताका विषय है। आकाश, हैं, उन भगवान्‌ श्रीकृष्णणो नमस्कार है। जो
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.13468)
- **Original**: सम्पूर्ण दिशाएँ और वायु भी यदि नष्ट हो जाय॑ँ तो समयपर संहर्ताका भी संहार करनेकी शक्ति रखते
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.13469)
- **Original**: भी पतिब्रताका शाप कभी नष्ट नहीं हो सकता*। हैं और अनायास ही स्रष्टाकी भी सृष्टि कर सकते
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.13470)
- **Original**: मेंरे शापसे यदि आप नष्ट हो जाते हैं तो सम्पूर्ण हैं, उन भगवान्‌ श्रीकृष्णको नमस्कार है। जो
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.13471)
- **Original**: सृष्टिका ही नाश हो जायगा। यह सोचकर मैं शत्रुकों भी मित्र बना सकते हैं, कलहको भी
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.13472)
- **Original**: किंकर्तव्यविमूढ़ हो रही हूँ; तथापि आपसे न्‍कहती उत्तम प्रेममें परिणत कर सकते हैं तथा सृष्टि और
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.13473)
- **Original**: हूँ। देवेश्वर ! जैसे पूर्णिमाकों चन्द्रमा पूर्ण होते हैं, विनाशकी भी क्षमता रखते हैं; उन भगवान्‌
- **Translation**: 

---

